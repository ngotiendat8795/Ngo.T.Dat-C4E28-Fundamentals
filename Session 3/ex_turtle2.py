from turtle import *

colors = ["red", "yellow", "blue", "grey", "cyan", "purple"]

def filled_object(wth, lth, clr):
    color(clr)
    for i in range(2):
        begin_fill()
        forward(lth)
        left(90)
        forward(wth)
        left(90)
        end_fill()

wth = int(input("Nhap chieu rong: "))
lth = int(input("Nhap chieu dai: "))

for clr in colors:
    filled_object(wth,lth,clr)
    forward(lth)

mainloop()