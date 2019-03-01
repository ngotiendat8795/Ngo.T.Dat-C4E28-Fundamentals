# r1 = range(1000,100,-5)
# print(*r1)

# for i in range(4):
#     print(i)

# for i in [0,1,8,3,"x"]:
#     print("hi")


# x=0
# for i in range(1,11,1):
#     x=x+i
# print(x)

# i = range(1,11)
# y = sum(i)
# print(y)

from turtle import *
speed(0)
shape('turtle')
forward(20)
x=20
for i in range(50):
    left(90)
    x=1.1*x
    forward(x)
mainloop()