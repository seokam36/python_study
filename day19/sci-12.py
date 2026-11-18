## lightGBM 튜닝 / 서빙 : 은행 고객 이탈(churn) 예측 - 이진 분류
import warnings
warnings.filterwarnings('ignore', message=".*'eval_set' is deprecated.*")

import pandas as pd

df = pd.read_csv('Bank Customer Churn Prediction.csv')
# 데이터 확인 : 10000행 , 결측치 0 , 중복 0
print(df.shape)
print(df.duplicated().sum())  # 중복행 개수
print(df.isna().sum())        # 결측치(빈 칸) 개수

num_cols = ['credit_score', 'age', 'tenure', 'balance', 'products_number',
            'credit_card', 'active_member', 'estimated_salary']  # 수치형
cat_cols = ['country', 'gender']                                 # 범주형

# 범주형 자료들을 원핫인코딩이 아닌 판다스'카테고리' 타입 변경 # lightGBM 내장 범주형 처리 사용 목적
for col in cat_cols:
    df[col] = df[col].astype('category')
X = df[num_cols + cat_cols]   # customer_id 는 식별자라 제외
Y = df['churn']               # 0 유지 / 1 이탈 (이탈 약 20% → 불균형)
from sklearn.model_selection import train_test_split
# 분류 문제이므로 stratify=Y : 훈련/테스트 모두 이탈 비율 20% 유지
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.2, stratify=Y)

# 1) 튜닝 -> optuna
# 2) optuna 로그 숨기기/경고만 출력
import optuna
from lightgbm import LGBMClassifier, early_stopping
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score

optuna.logging.set_verbosity( optuna.logging.WARNING )

# 4) 목적함수 만들기: 각 탐색 시도 마다 교차 검증 수행 후 평균 성능 반환, *콜백함수( trial )
def objective( trial ) :
    # 4-1 교차검증 StratifiedKFold : 분류 문제라 폴드마다 이탈 비율 유지
    cv = StratifiedKFold( n_splits=5 , shuffle=True, random_state=42 )
    cv_f1_scores = [ ]      # 각 폴드별 검증 점수 저장
    best_iterations = [ ]   # 각 폴드별 최적 트리 번호 저장
    for train_idx, val_idx in cv.split( X_train , Y_train ) :
        # K번째 폴드의 훈련용/검증용 인덱스 반환
        # 훈련 데이터 세트 내부에서 훈련용/검증용 분할 수행 , K=5 , 5개 폴드, 각각 한번씩 검증용
        X_tr, X_val = X_train.iloc[ train_idx ] , X_train.iloc[val_idx]
        Y_tr, Y_val = Y_train.iloc[ train_idx ] , Y_train.iloc[val_idx]
        # k폴드에서 분할한 훈련용 모델 만들기
        model = LGBMClassifier(
            n_estimators=1000,
            # trial.suggest_XXX( '파라미터명' , 시작값, 끝값 )
            learning_rate=trial.suggest_float( 'learning_rate' , 0.01 , 0.1 , log=True ) ,
            num_leaves=trial.suggest_int( 'num_leaves' , 8, 30 ),
            max_depth=trial.suggest_int( 'max_depth' , 3 , 6 ),
            min_child_samples=trial.suggest_int( 'min_child_samples', 30 , 150 ),
            subsample=trial.suggest_float( 'subsample' , 0.6 , 1.0 ) ,
            subsample_freq=1, verbose=-1, random_state=42, n_jobs=-1 ,
            colsample_bytree=trial.suggest_float( 'colsample_bytree' , 0.6 , 1.0 ),
            class_weight='balanced',   # 분류 모델 이므로 불균형 보정 (이탈 20%)
        )
        # 4-2 교차별 학습 모델
        # K폴드별 훈련용/검증용 으로 학습
        model.fit( X_tr , Y_tr , eval_set=[ (X_val,Y_val) ] ,
                   callbacks=[ early_stopping( stopping_rounds=50, verbose=False ) ] )

        # 4-3 교차별 학습 성능 저장
        # K폴드별 검증 평가 f1 (분류 model.score 는 정확도라서 f1_score 직접 계산)
        f1 = f1_score( Y_val , model.predict( X_val ) , average='macro' )
        cv_f1_scores.append( f1 )                       # k폴드별 평가 점수 저장
        best_iterations.append( model.best_iteration_ ) # k폴드별 최적 트리 번호 저장
    # k폴드에서 산출된 최적 트리 개수의 평균값을 trial의 속성으로 저장
    trial.set_user_attr( 'best_n_estimators' , int( np.mean( best_iterations ) ) )
    return np.mean( cv_f1_scores ) # 검증 평가 평균 점수 반환

# 3) optuna.create_study( direction='maximize/minimize' )
# 현재 실습은 분류모델이며 f1-score(macro) 평가지표 사용 → 클수록 좋음
sampler = optuna.samplers.TPESampler( seed=42 )
study = optuna.create_study( direction='maximize' , sampler= sampler )
# study.optimize( 목적함수 , n_trials=반복수 )
study.optimize( objective , n_trials=30 ) # -> 반복 수 만큼 목적함수 실행

# 5) 최적 모델
print( '최적 하이퍼파라미터:', study.best_params )
best_n_estimators = study.best_trial.user_attrs['best_n_estimators']
print( '최적 트리: ', best_n_estimators )
print( '교차검증 F1: ', round( study.best_value, 4 ) )
# 최적 하이퍼파라미터: {'learning_rate': 0.048, 'num_leaves': 19, 'max_depth': 6, 'min_child_samples': 42, 'subsample': 0.775, 'colsample_bytree': 0.664}
# 최적 트리:  465
# 교차검증 F1:  0.7524

# 6) 최적 파라미터로 모델 학습
final_model = LGBMClassifier(
    random_state=42, verbose=-1, n_jobs=-1,
    subsample_freq=1, class_weight='balanced',   # 튜닝 때와 같은 조건
    **study.best_params, # 최적 파라미터 포함 , 전개 연산자
    n_estimators=best_n_estimators
)
final_model.fit(X_train, Y_train)
from sklearn.metrics import classification_report
Y_pred = final_model.predict(X_test)
test_f1 = f1_score(Y_test, Y_pred, average='macro')
print('train f1 : ', f1_score(Y_train, final_model.predict(X_train), average='macro')) # train f1 :  0.8499
print('test f1 : ', test_f1)                                                           # test f1 :  0.7478
print(classification_report(Y_test, Y_pred, target_names=['유지', '이탈']))
# 특성 중요도 : 기본값(split)은 분기 횟수라 0/1 특성이 낮게 나옴 → gain(오차를 줄인 양) 기준
print(final_model.feature_name_)
print(final_model.booster_.feature_importance('gain'))

# 7) joblib 저장/로드
import joblib
joblib.dump(final_model, 'model.pkl')
# 성능 지표 + 학습 때 범주 목록(서버에서 범주 맞출 때 사용) 따로 저장
joblib.dump({'f1': round(test_f1, 4),
             'cv_f1': round(study.best_value, 4),
             'best_params': study.best_params,
             'cat_dtypes': {col: X_train[col].dtype for col in cat_cols}},
            'metrics.pkl')
model = joblib.load('model.pkl')
metrics = joblib.load('metrics.pkl')

# 8) 예측
new_customers = pd.DataFrame([
    {'credit_score': 650, 'age': 45, 'tenure': 3, 'balance': 120000.0, 'products_number': 1,
     'credit_card': 1, 'active_member': 0, 'estimated_salary': 90000.0,
     'country': 'Germany', 'gender': 'Female'}
])
# 범주형 카테고리 매핑 일치를 위해 학습 때 dtype 으로 변환 (practice6 방식)
for col in cat_cols:
    new_customers[col] = new_customers[col].astype(metrics['cat_dtypes'][col])
new_customers = new_customers[num_cols + cat_cols]   # 열 순서도 학습 때와 같게

preds = model.predict(new_customers)
proba = model.predict_proba(new_customers)
print('서빙 모델 예측 (1번고객) 이탈:', preds[0])        # 1
print('서빙 모델 예측 (1번고객) 이탈 확률:', proba[0][1]) # 0.89