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
plt.plot(epochs, train_loss, label="Train Loss", color="blue", linestyle="-", marker="o")
plt.plot(epochs, val_loss, label="Val Loss", color="mediumaquamarine", linestyle="--", marker="s")

plt.title("학습별 모델 손실 추세") # 차트의 제목
plt.xlabel("학습수") # x축 제목
plt.ylabel("손실")  # y축 제목
plt.grid(True)      # 구분선
plt.legend()        # 범례 표시

plt.show() # 차트실행

# 2] 막대 차트(비교)