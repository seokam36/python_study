# Practice8: API 데이터 수집
# 1. 개요 및 대상 API 정보
# API 이름: 행정안전부_착한가격업소 현황
# API URL: https://www.data.go.kr/data/3045247/fileData.do
import httpx
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

service_key = "07ba92edfcaee38ad71678c2d4af00daed24f106e40933bde077d9a3398d9536"

# 목표: httpx를 통해 공공데이터 API를 호출하고, pandas를 활용해 업소명, 주소, 가격 데이터를 구조화한 뒤 통계 분석을 수행합니다.
# 2. 상세 요구사항
# 2-1 (API 호출 및 파라미터 설정):
# 지정된 API URL에 인증키(serviceKey)를 포함하여 요청합니다.
# 임의의 100건의 데이터를 수집
def test1():
    url = "https://api.odcloud.kr/api/3045247/v1/uddi:1c782e6f-9281-451d-aa04-a550074abc2d"
    url += "?page=1&perPage=100"
    url += f"&serviceKey={service_key}"

# 2-2 (데이터프레임 적재):
# 응답받은 JSON 데이터 중 실제 행 목록인 data 배열을 추출하여 pandas.DataFrame으로 변환합니다.
    response = httpx.get(url)
    response_json = response.json()
    data_frame = pd.DataFrame(response_json['data'])
    data_frame.info()

# 2-3 (데이터 전처리 및 분석):
# 가격1 컬럼의 데이터를 숫자형(pd.to_numeric)으로 변환합니다.
# 수집된 100건 데이터 기준 가격1의 평균값을 산출하여 출력합니다.
    # info()에서 전부 object로 나오면 문자열이라는 뜻 -> to_numeric으로 숫자 변환
    # errors='coerce': 변환 못 하는 값(빈 문자열 등)은 NaN 처리, mean()은 NaN을 자동 제외
    data_frame['가격'] = pd.to_numeric(data_frame['가격'], errors='coerce')
    print(data_frame['가격'].mean())

# 2-4 (업종별 평균 가격 집계 및 시각화):
# groupby('업종')을 사용하여 업종별 가격1의 평균 가격을 계산합니다.
# seaborn의 barplot 및 matplotlib을 활용하여 업종별 평균 가격 비교 막대그래프를 시각화합니다.
    mean = data_frame.groupby('업종')['가격'].mean().reset_index()
    sns.barplot(data=mean, x='업종', y='가격')
    plt.show()

test1()