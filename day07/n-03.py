import numpy as np

# 1. 병합 , np.vstack([배열1],[배열2]) , np.hstack([배열1],[배열2])
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.vstack([x,y])
print(z)    #[[1 2][3 4][5 6][7 8]] -> 세로로 병합

z = np.hstack([x,y])
print(z)    #[[1 2 5 6]
            #[3 4 7 8]]

# 2. 병합2 , np.concatenate((배열1,배열2), axis=?)
z = np.concatenate((x,y), axis=0) # axis=0 세로병합
print(z)
z = np.concatenate((x,y), axis=1) # axis=1 가로병합
print(z)

# 3. 정렬 , np.sort(배열) : 오름차순
x = np.array([3,1,4,2,5])
print(np.sort(x))
print(np.sort(x)[::-1]) # 슬라이싱 이용해서 내림차순
print(x)    # 원본 변경 안됨

x.sort()    # 배열.sort()
print(x)    # 원본 자체 변경됨

# 4. np.argsort(배열) , 정렬했을 때 각 자리에 올 원래 위치
scores = np.array([39, 89, 30, 92])
z = np.argsort(scores) # [2 0 1 3] -> 오른차순 기준으로 정렬했을 때 각 위치 번호
print(z)
print(z[-1])

# 5. 필터링/조건식 ,
x = np.array([10, 20, 30, 40, 50])
print(x>30) # [False False False  True  True]
print(x[x>30]) # [40 50] -> 인덱싱 안에서 조건식 사용하면 True 값 추출

y = np.array([[1,2,3] , [4,5,6]])
print(y%2==0) #[[False  True False]
              #[ True False  True]]
print(y[y%2==0]) # [2 4 6]

# 6. 삼항연산자 , np.where(조건, 참, 거짓)
print(np.where(x>30, x, 0)) # [ 0  0  0 40 50]
print(np.where(y%2==0 , 0, 1)) # [[1 0 1]
                                    # [0 1 0]]

# 7. 다수 조건 , & | ~
# 조건 두개 이상일때 ( ) 또는 변수 사용
a = y%2==0
print(y[a & (y%4==0)]) # 짝수이면서 4의배수
print(y[a | (y%4==0)]) # 짝수이거나 4의배수
print(y[~a]) # 짝수가 아닌 홀수

# 넘파이는 파이썬에서 실행 되는 구조( 중복에 따른 오버라이딩 제한 ) bool vs bool_