print("hello")

# 70p.
import keyword
print(keyword.kwlist)

# 77p. 출력하기
# 하나만 출력
print("하나만 출력합니다")
# 여러 개 출력 , 주의 : ,쉼표 기준으로 공백 자동 포함
print("여러개","출력합니다")
print() # 한줄 공백 , 추후에 제어문자 \n

# 85p. 타입 확인하기
print(type(-1))
print(type(True))
print(type(None))
print(type([]))
print(type({}))
print(type(()))

# 86p. 문자열만들기
print("AB")
print('AB')
print("""a
b
c""")
print("'a''b''c'")
print('"a""b""c"')
print("\"A\'B\nC\t\\E")

# 93.p 문자열 연산
# 1. + 연결연산자
print("안녕"+"하세요")
# 주의 : 문자열과 숫자 연결 불가능
# 2. * 반복연산자
print("안녕"*3)
# 3. 인덱싱 , 문자열은 배열이므로 인덱스 존재
print("안녕하세요"[0]) # 안
print("안녕하세요"[-1]) # 요 , 역순 인덱스
print("안녕하세요"[-3]) # 하
# 4. 슬라이싱 , 문자열 자르기 , [시작인덱스:끝인덱스]
print("안녕하세요"[0:2]) # 0~1
print("안녕하세요"[1:3]) # 1~2
# 시작인덱스 생략시 0 , 끝인덱스 생략하면 마지막 인덱스
print("안녕하세요"[1:]) # 1~끝까지
print("안녕하세요"[:3]) # 0~2
# 5. 문자열의 길이 , len(문자열)
print(len("안녕하세요"))

