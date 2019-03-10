# #1
# def Hello_world(n):
#     for i in range(n):
#         print("Hello world!")

# Hello_world(3)

# #2
# def sum(a,b):
#     print(a+b)

# sum(2,3)

# #3
from turtle import *
# def square(length, clr):
#     color(clr)
#     for i in range (4):
#         forward(length)
#         left(90)

# for i in range(30):
#     square(i*5, 'red')
#     left(17)
#     penup()
#     forward(i * 2)
#     pendown()

#4
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

speed(0)
color('blue')
for i in range(150):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()