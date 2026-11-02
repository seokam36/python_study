# 웹 크롤링 : 웹페이지 존재하는 데이터들을 수집 하는 기술
# HTML / CSS 기초 지식
# 파이썬 크롤링 라이브러리 : 정적(request/BeautifulSoup), 동적(Seleium, playwright)
# 확인
    # 1. 크롤링할 페이지의 도메인주소/robots.txt
    # User-agent:사용자/브라우저/AI, Disallow : 불가능 , Allow : 가능
    # 2. 개발자도구

# 설치 : C:\venvs\py314\Scripts\python.exe -m pip install requests
# 설치 : C:\venvs\py314\Scripts\python.exe -m pip install beautifulsoup4

# 1] 네이버 검색 정보 크롤링( 정적 )
# 1. 크롤리 주소 가져오기 , *파라미터 정리*, ?쿼리스트링
url = "https://search.naver.com/search.naver?&query=안양날씨"

# 2. requests 라이브러리로 해당 주소 요청하기
import requests                 # URL 요청 라이브러리

response = requests.get(url)
# print(response)

# 3. 요청 성공했으면 요청한 페이지의 HTML 파싱 하기
from  bs4 import BeautifulSoup  # 요청된 URL의 HTML 파싱 라이브러리

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

# 4. 파싱한 이유 : 특정한 식별자(마크업)의 텍스트 추출
# soup.select( 선택자 )
text = soup.select_one(".temperature_text")
print(text)

# 5. 마크업 사이의 텍스트 추출
# 추출한DOM.get_text()
print(text.get_text())