import numpy as np
data = np.genfromtxt('./경찰청_연도별 사이버 범죄 통계 현황_20251231.csv', delimiter=',', skip_header=1)
np.set_printoptions(suppress=True, precision=2)

# step1.
occ = data[0::2,:] # 발생건수
arr = data[1::2,:] # 검거건수
occ_crime = occ[:,2:] # 발생건수별 범죄
arr_crime = arr[:,2:] # 검거건수별 범죄
occ_arg = np.mean(occ_crime, axis=0) # 발생건수 종류별 평균
arr_arg = np.mean(arr_crime, axis=0) # 검거건수 종류별 평균
print(occ_arg)
print(arr_arg)

# step2.
occ_year = occ[:,0] # 발생건수 년도
arr_year = arr[:,0] # 검거건수 년도
occ_over = occ_crime > occ_arg # 발생건수 > 발생건수 평균
arr_over = arr_crime > arr_arg # 검거건수 > 검거건수 평균
print(occ_year[occ_over[:,0]]) # 발생건수의 첫번째 열(해킹_계정도용)의 True값의 년도 추출
print(arr_year[arr_over[:,0]]) # 검거건수의 첫번째 열(해킹_계정도용)의 True값의 년도 추출


