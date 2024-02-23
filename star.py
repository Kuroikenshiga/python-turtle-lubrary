from turtle import *
from math import *
from random import *
pencolor('pink')
bgcolor('black')
pensize(2)
def triangle(reversed = False,yAxle = 0):
    penup()

    sety(yAxle)
    pendown()
    for i in range(0,3):
        forward(100)
        left(120 if not reversed else -120)
        
    
triangle()
triangle(True,yAxle=65)
penup()
sety(32.6)
setx(-20)
pendown()
left(-90)
circle(70)
mainloop()