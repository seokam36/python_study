# 맷플롯립 : 파이썬에서 시각적으로 표현하는 라이브러리
# 설치 : pip install matplotlib
import matplotlib.pyplot
print(matplotlib.__version__)

import matplotlib.pyplot as plt
# 맷플롯립 그래프는 한글폰트 지원 안한다
plt.rc('font', family='Malgun Gothic')  # 윈도우 맑은고딕으로 설정
plt.rcParams['axes.unicode_minus'] = False    # 음수 기호 깨짐 방지

# 1] 선 차트 (추세)
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23, 0.20]
val_loss = [0.95, 0.75, 0.60, 0.52, 0.48, 0.45, 0.44, 0.43, 0.44, 0.45]

# 1.1 차트의 전체 크기 설정 -> plt.figure(figsize=(가로inch, 세로inch))
plt.figure(figsize=(7, 4))

# 1.2 축 -> plt.plot(x축값, y축값, label="계열명", color="색상명", linestyle="선종류", marker="마커종류")
# plt.plot(epochs, train_loss, label="Train Loss", color="blue", linestyle="-", marker="o")
# plt.plot(epochs, val_loss, label="Val Loss", color="mediumaquamarine", linestyle="--", marker="s")
#
# plt.title("학습별 모델 손실 추세") # 차트의 제목
# plt.xlabel("학습수") # x축 제목
# plt.ylabel("손실")  # y축 제목
# plt.grid(True)      # 구분선
# plt.legend()        # 범례 표시


 # plt.show() # 차트실행

# # 2] 막대 차트(비교)
# classes = ['Cat', 'Dog', 'Bird', 'Fish']
# counts = [120, 150, 80, 45]
#
# # 2.1 plt.bar(x값, y값, color=[색상], width=막대크기)
# bars = plt.bar(classes, counts, color=['#3EE489', '#E17055', '#3498DB', '#00B894'], width=0.5)
#
# # 2.2 막대 값 레이블 -> plt.bar_label(막대차트변수, padding=막대와레이블간격, fontsize=폰트크기)
# plt.bar_label(bars, padding=3, fontsize=8)
#
# plt.title('클래스별 샘플수')
# plt.xlabel('클래스')
# plt.ylabel('샘플 수')
# plt.grid(True, alpha=0.5) # alpha=투명도
#
# plt.show()

# 3] 산점도(상관관계)
# x = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
# y = [2.3, 3.8, 5.1, 7.0, 7.8, 9.2, 10.5]
#
# # 3.1 산점도 -> plt.scatter(x축값, y축값, color="색상", s=점크기, alpha=투명도)
# plt.scatter(x, y, color='#3EE489', s=80, alpha=0.8)
# plt.title('공부시간과 시험점수의 상관관계')
# plt.xlabel('공부시간')
# plt.ylabel('시험점수')
#
# plt.show()

# # 4] 히스토그램(연속형 수치/값 분포)
import numpy as np
#
# # 평균 170을 중심으로 표준편차 5만큼 퍼져 있는 종모양(가우시안분포) 난수 1000개
# heights = np.random.normal(loc=170, scale=5, size=1000)
#
# # 4.1 히스토그램 -> plt.hist(값, bins="구간개수", edgecolor="테두리색상")
# plt.hist(heights, bins=30, edgecolor="black")
# plt.xlabel("키(cm)")
# plt.ylabel("빈도/분포 수")
#
# plt.show()

# 5] 박스플롯(분포 범위내 이상치)
heights = np.random.normal(loc=170, scale=5, size=1000)
data_with_outliers = np.append(heights, [210, 215, 120])

# 5.1 박스플롯 -> plt.boxplot(값) , 데이터들을 사분위수(25%, 50%, 75%) 표현
plt.boxplot(data_with_outliers)


# 6] 한 창에 2개 이상 그래프 표현 -> fig, axs = plt.subplots( 행개수, 열개수, figsize=(가로,세로))
fig, axs = plt.subplots( 1, 2, figsize=(10, 4))

# 1행 1열 차트
axs[0].plot([1,2,3] , [4,5,6])
axs[0].set_title('서브1: 선그래프')
# 1행 2열 차트
axs[1].bar(['A','B','C'], [30,10,20])
axs[1].set_title('서브2: 막대그래프')
plt.show()