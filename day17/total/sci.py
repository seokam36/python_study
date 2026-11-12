import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures

df = pd.read_csv('insurance.csv')

print(df.shape) # (1338, 7)
print(df.head()) # 컬럼확인
print('결측:',df.isnull().sum()) # 결측치 확인
print('중복:',df.duplicated().sum()) # 중복행 확인
df = df.drop_duplicates() # 중복행 제거
# df.info()

X = df.drop(columns=['charges'])
Y = df['charges']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

num_cols = ['age', 'bmi', 'children']
cat_cols = ['sex', 'smoker', 'region']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(drop='first'), cat_cols),
])

pipe = Pipeline([
    ('prep', preprocessor),
    ('poly', PolynomialFeatures(include_bias=False)),
    ('model', Ridge(random_state=42)),
])

param_grid = {'model__alpha': [0.01, 0.1, 1, 10, 100],'poly__degree': [1, 2, 3]}
grid = GridSearchCV(pipe, param_grid, cv=5, scoring='r2')
grid.fit(X_train, Y_train)

best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)
test_r2 = r2_score(Y_test, y_pred)

print('R2 테스트:', test_r2)
print('최적 파라미터:', grid.best_params_)
print('R2 best Score: ', grid.best_score_)


joblib.dump(best_model, 'insurance.pkl')

metrics = {
    'test_r2'     : round( best_model.score( X_test , Y_test ) , 4 ) ,   # 테스트(검증) 데이터 R²
    'cv_r2'       : round( float( grid.best_score_ ) , 4 ) ,             # 교차검증 평균 R²
    'best_params' : grid.best_params_                                    # 최적 파라미터
}

joblib.dump( metrics , 'insurance_metrics.pkl' )



