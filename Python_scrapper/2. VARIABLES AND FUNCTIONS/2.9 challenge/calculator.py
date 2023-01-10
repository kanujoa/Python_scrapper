def add(a="Please input", b=" an argument."):
    print(a + b)     # 문자열은 더할 수 있기 때문에 add 함수에서 default 값으로 사용 가능.

def sub(a=False, b=False):
    print(a - b)

def div(a=0, b=1):
    print(a / b)

def mul(a=0, b=1):
    print(a * b)     # 문자열 곱하기도 가능하기 때문에 mul 함수에서 default 값으로 사용 가능.

def squ(a=False, b=True):
    print(a ** b)

# 함수에 들어 있는 연산을 수행하기 때문에 그에 맞게 오류가 나지 않는 자료형과 방식을 이용해 default 값을 설정해야 한다. 
add()
sub()
div()
mul()
squ()

add(1, 3)
sub(5, 2)
div(9, 3)
mul(4, 6)
squ(7, 2)