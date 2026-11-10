import pandas as pd

df = pd.read_csv('Fish.csv') # 1) 자료 수집
X = df [['Length2', 'Height', 'Width']] # # 2) 예측!!할 특성과 타깃 선정/구성
Y = df ['Weight'] # 3) 타깃(정답) 선정/구성
# 4) 훈련/테스트 분리
from sklearn.model_selection import train_test_split, KFold, GridSearchCV

X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

# 5) 과소적합 방지 하고자 항 추가 PolynomialFeatures
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)

# 6) 항 많아지면 항/특성 간에 단위 표준화/스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train_poly)
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)

# 7) 모델 선택 = 단순선형회귀, 규제(릿지/라쏘) alpha 규제강도
from sklearn.linear_model import LinearRegression, Ridge

model = LinearRegression()
model.fit(X_train_scaled,Y_train)

# 8) 결정계수
print('r2:',model.score(X_test_scaled, Y_test))
print('r2:',model.score(X_train_scaled, Y_train))


# ============ 과정 묶음
from sklearn.pipeline import Pipeline

# pipe_model = Pipeline([ ('식별자', 클래스명) ])
pipe_model = Pipeline([ ('poly', PolynomialFeatures(degree=2, include_bias=False) ),
                        ('scaler', StandardScaler() ),
                        ('regressor', LinearRegression() )])
# 9) 파이프라인으로 학습
pipe_model.fit(X_train, Y_train)
print('r2:',pipe_model.score(X_test, Y_test))
print('r2:',pipe_model.score(X_train, Y_train))

# 10) 최적(성능좋은/오차적은)의 파라미터(매개변수/대입값) 찾기
# degree=2, alpha=0.1
# 1. 파이프라인 만들기
pipe_model = Pipeline([('poly',PolynomialFeatures(include_bias=False)), # degree 튜닝
                        ('scale', StandardScaler()),
                        ('ridge',Ridge())   # alpha 튜닝
                       ])
# 2. 후보군 파라미터 만들기 , {'식별자__파라미터명' : [후보값, 후보값]}
param_grid = {'poly__degree' : [2, 3], 'ridge__alpha' : [0.001, 0.01, 0.1, 1, 10, 100]}

# 3. k-fold 교차 검증
# kf = KFold(n_splits= k개의 동일한 폴드로 분할, shuffle=분할시 무작위 섞기, random_state=42)
kf = KFold(n_splits=5, shuffle=True, random_state=42)
# 학습 데이터들을 5개로 나누어 4개학습하고 1개로 검증 하는 과정을 5번 교차 검증 = 평균 오차/손실 성능

# 4. 그리드서치CV : 교차검증과 다양한 파라미터 자동으로 실행하고 최적 성능 찾기
# GridSearchCV( estimator=진행할모델/파이프라인, param_grid={파라미터후보군}, scoring='평가지표명', cv=교차검증, n_jobs=-1 )
grid = GridSearchCV(
    estimator=pipe_model,
    param_grid=param_grid,
    scoring='r2',
    cv= kf,
    n_jobs=-1
)

# 5. 그리드서치로 학습
grid.fit(X_train, Y_train)

# 6. 주요 속성
best_model = grid.best_estimator_ # 가장 성능 좋은 모델 반환
print(grid.best_params_) # 가장 성능 좋은 파라미터 조합
print( grid.best_score_) # 교차 검증에서 평균 점수

# 7. 최적 모델로 평가
print('r2: ', best_model.score(X_train, Y_train))

# 11) 서빙, 학습된 모델 저장하고 다른곳에서 호출
# 연구/학습 : 코랩(고사양)에서 학습 --> 실제 서버(FAST API)에서 호출
# 실무: GPU서버 학습 --> 실제 서버에서 호출
import joblib
# joblib.dump(저장할모델, 경로)
joblib.dump(best_model, 'fish_model.pkl')

# 12) 다른 파이썬 파일에서 저장된 모델 불러오기
