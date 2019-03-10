from random import randint
from random import choice

def calculator(x,y,op):

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    else:
        result = x/y
    return result

ketqua = calculator(8,3,"/")

print(ketqua)

x = randint(1,10)
y = randint(1,10)
op = choice(["+", "-", "*", "/"])

print("{0} {2} {3} = {4}").format(x,op,y)

