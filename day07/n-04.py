import numpy as np

# 1. 1차원 배열 통계 함수
x = np.array([1,2,3,4,5])
print(np.min(x), np.max(x)) # 최솟값, 최댓값
print(np.argmin(x), np.argmax(x)) # 최솟값위치, 최댓값위치
print(np.sum(x), np.mean(x) , np.median(x)) # 합계, 평균, 중앙값
print(np.var(x)) # 분산 : 요소 값들이 떨어진 정도
print(np.std(x)) # 표준편차 : 분산에 양의 제곱근 사용하여 데이터 단위 맞춘 값
print(np.sqrt(x)) # 양의 제곱근 (루트)

# 2. 2차원 배열 통계 함수
# np.통계함수( 2차원배열, axis = 생략 -> 1차원평탄화 / 0 -> 열마다 / 1 -> 행마다 )
y = np.array([ [1,2,3] , [4,5,6] ])
print(np.min(y), np.max(y)) # 1 6
print(np.min(y , axis=0) , np.max(y, axis=1)) # axis=0 열마다, axis=1 행마다
print(np.argmax(y, axis=1))
print(np.sum(y, axis=1), np.mean(y, axis=0), np.median(y, axis=1))
print(np.var(y))