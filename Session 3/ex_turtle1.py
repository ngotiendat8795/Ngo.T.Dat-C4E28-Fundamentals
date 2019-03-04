from turtle import *

colors = ["red", "yellow", "blue", "grey", "cyan"]
num_sides = [3, 4, 5, 6, 7]
def draw_object(num_side, side_length, clr):
    color(clr)
    for i in range(num_side):
        forward(side_length)
        left(360/num_side)

side_length = int(input("Nhap do dai canh: "))

for clr in colors:
    id = colors.index(clr)
    num_side = num_sides[id]
    draw_object(num_side, side_length, clr)

mainloop()