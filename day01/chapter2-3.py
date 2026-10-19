# 115p.
pi = 3.1415
r = 10
print(pi, r)

# 118p. 입력함수, 반환타입 : 문자열
input("인사말을 입력하세요>")
string = input("입력> ") # 입력받은값 변수에 저장
print(type(string))  # 123 -> str, 안녕 ->str

# 121p. 타입변환 , str -> int/float
string_int = int(string)
string_float = float(string)
print(type(string_int), type(string_float))
# 주의 : "a3" 숫자타입 변환 X, 소수점있는 문자열은 int 변환 X

# 125p. 누적예제
raw_input = input("inch 입력 >")
inch = int(raw_input)
cm = inch * 2.543
print(cm)

# 135p. "문자열".format(값)
string_a = "age:{}".format(10)
print(string_a)
string_b = "{} {} {}".format(1,"d",True)
print(string_b)

