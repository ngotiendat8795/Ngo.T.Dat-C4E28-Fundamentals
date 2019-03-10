from random import randint
from random import choice

minn = int(input('Min: '))
maxx = int(input('Max: '))

x = randint(minn,maxx)
y = randint(minn,maxx)

# operat = input("what kind of opeartor do you want to carry out, CONG, TRU, NHAN, CHIA:").upper()

Matrix = {
    "+" : x+y,
    "-" : x-y,
    "*" : x*y,
    "/": x/y
}

list_key = []
for key in Matrix:
    list_key.append(key)

Cal = choice(list_key)
correct_answer = Matrix[Cal]
wrong_answer = randint(minn*minn, maxx*maxx)

RW = choice([wrong_answer,correct_answer])

#print("{0} {1} {2}").format(x,y,..)
print(x,Cal,y,"=",RW)
yn_input = input("Y/N?").upper()

loop = True
while loop:

    if yn_input == "Y":
        if RW == wrong_answer:
            print("wrong!")
        else:
            print("right!")
        loop = False

    elif yn_input == "N":
        if RW == wrong_answer:
            print("right!")
        else:
            print("wrong!")
        loop = False

    else:
        print("Re-enter your answer in Y or N: ")



# print("Answer: ", Matrix[operat])

x = randint(1,10)
y = randint(1,10)
op = choice (["+","-","*","/"])
error = randint(-2,2)

from cal_func import calculator
real_result = calculator(x,y,op)

real_result = cal_func.calculator(x,y,op)

dis_result = real_result + error




