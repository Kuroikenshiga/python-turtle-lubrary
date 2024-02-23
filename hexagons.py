from turtle import *
from math import *
from random import *
speed(0)
pensize(2)
bgcolor('gray')
colors = ["red","pink","blue","green","yellow",]
colorIndex = 0
for k in range(1,71):
    for i in range(1, 7):
        if(colorIndex == len(colors)):
            colorIndex = 0
        pencolor(colors[colorIndex])
        colorIndex = colorIndex+1
        forward(100)
        left(60)
        
    left(5)

mainloop()