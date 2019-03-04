from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
k = 3
for i in colors:
    color(i)
    for i in range(k):
        forward(100)
        left(360/k)
    k = k + 1
mainloop()