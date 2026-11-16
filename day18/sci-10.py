# 부스팅 앙상블
# 설치 : pip install lightgbm xgboost catboost
import time

from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'

import pandas as pd

df = pd.read_csv(url)
# alcohol, sugar, pH, class(0:레드 / 1:화이트)
X = df[['alcohol', 'sugar', 'pH']]
Y = df['class']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

# 3가지 부스팅 앙상블
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

# 1) 모델 비교
# n_estimators : 부스팅 사용할 트리 개수 기본값 100, 권장 1000~3000
# learning_rate : 학습률, 경사하강법에서 오차 보정 하기 위한 이동 단위
# verbose=-1 : 실행중 트리들이 처리하는 로그 끄기
models = {
    "XGBoost" : XGBClassifier(n_estimators=100, learning_rate=0.05, max_depth=4,
                              random_state=42, n_jobs=-1),
    "LightGBM" : LGBMClassifier(n_estimators=100, learning_rate=0.05, max_depth=4,
                            random_state=42, n_jobs=-1, rerbose=-1)
}

# 2) 반복 이용하여 모델 학습 / 학습 시간 테스트
for name, model in models.items():
    start = time.time() # 학습 시작 시간
    model.fit(X_train,Y_train)
    end = time.time() - start # 현재 시간에서 시작시간 제외
    Y_pred = model.predict(X_test)

    print('=========== 모델명 : ', name)
    print('> 학습 소요시간 : ', end, '초')
    print('> Train Acc : ', model.score(X_train, Y_train))
    print('> Train Acc : ', model.score(X_test, Y_test))
    print('> f1 score : ', f1_score(Y_test, Y_pred, average='macro'))