# 비교연산자

# 158p. 범위 논리
x = 25
print(10 < x < 30)
# 논리연산자
    # not , and , or
print( not True)
print(True and True)

# 163p. if 조건문
# if ~ else
age = 10
if age >= 19 :
    print("성인")
else:
    print("미성년자")

# if ~ elif ~ elif ~ else
if age >= 20:
    print("A")
elif age >= 30:
    print("B")
else:
    print("C")

# if 중첩
x=10
if x>5:
    if x>10:
        print("10보다 크다")
    else:
        print('5보다 크고 10보다 작거나 같다')
else:
    print('5보다 작거나 같다')

# 182p. False 되는 경우
# None, 0, 0.0, 빈문자열, 빈리스트, 빈객체 등
# 그외 True

x=10
y=2
if x>4:
    if y>2:
        print(x*y)
else:
    print(x+y)