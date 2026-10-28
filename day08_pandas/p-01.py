import pandas as pd
print(pd.__version__)

# 1] 데이터프레임 : 2차원(표) , pd.DataFrame(리스트 , columns=[''])
data_list = [ [ 'ant' , 25 , 'seoul'] , ['bee' , 30 , 'busan'] , ['cat' , 35 , 'incheon'] ] # 2차원 리스트
df = pd.DataFrame(data_list)
print(df) # 행 과 열 => 표 형식
df = pd.DataFrame(data_list, columns=['name', 'age', 'city'])
print(df)

# 2] 데이터프레임2, pd.DataFrame(딕셔너리)
data_dict = {
    'name' : ['ant','bee','cat'] ,
    'age' : [25,30,35] ,
    'city' : ['seoul','busan','incheon'] } # 딕셔너리
df = pd.DataFrame(data_dict)
print(df)

# 3] 컬럼 컬럼의 값들 추출, df['열이름']
ages = df['age'] # 나이 추출
print(ages)         # Series(1차원)
print(type(ages))   # <class 'pandas.core.series.Series'>
print(type(ages.values)) # <class 'numpy.ndarray'>

# 4] 데이터프레임3 , pd.DataFrame(data_list,columns=[''],index=[''])
import numpy as np
data_np = np.array(data_list) # 넘파이 자료
df = pd.DataFrame(data_list,
                  columns=['name','age','city'],
                  index=['A','B','C'])
print(df)

# 5] 주요 속성
print(df.shape) # 행/열 크기 (3, 3)
print(df.columns)
print(df.index)
print(df.values)
print(df.head(2))
print(df.tail(2))
df.info()

# 6] 인덱싱
print(df.iloc[0])
print(df.iloc[1,2])
print(df.loc['B'])
print(df.loc['B', 'city'])


