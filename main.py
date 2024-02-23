from turtle import *
from math import *
from random import *
# print(sqrt(20000))
bgcolor("black")
setDegrees = 90
colors = ["red","pink","blue","green","yellow",]
colorIndex = 0
speed(0)

pensize(3)
pencolor('purple')
for i in range(1, 241):
    forward(200)
    if(i%4 == 0):
        setDegrees = setDegrees + 1
        if(colorIndex == 5):
            colorIndex = 0
        pencolor(colors[colorIndex])
        colorIndex = colorIndex + 1
    left(setDegrees)
    
mainloop()
    

# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(135)
# forward(141)
# left(135)
# forward(100)
# left(135)
# forward(141)
# left(135)
# pencolor("red")
# forward(50)
# left(90)
# forward(100)
# right(90)
# forward(50)
# right(90)
# forward(50)
# right(90)
# forward(100)
