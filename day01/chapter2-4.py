# 137 ~ 140p. 생략

# 141p. 대소문자 변환
a = "Hello"
print(a.upper())
print(a.lower())

# 142p. strip() 양쪽 여백/공백 제거
a = " hello python "
print(a.strip())

# 143p. isOOO() 구성 확인 , 반환타입 : True / False
print("Hello".isalpha())

# 144p. find() , 없으면 -1 있으면 인덱스반환
output_a = "안녕안녕하세요".find("안녕")
print(output_a)
# rfind() , 오른쪽 부터 기준
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
output_c = "안녕안녕하세요".find("h")
print(output_c)

# 145p. 찾을값 in 문자열 , 없으면 False 있으면 True
print("안녕" in "안녕하세요")
# 문자열.split(기준문자)
a = "10 20 30".split(" ")
print(a)

# 146p. f-문자열
a = 1
print(f"a:{a}") # a:1