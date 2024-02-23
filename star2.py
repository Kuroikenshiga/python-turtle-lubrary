from turtle import *
from math import *
from random import *
from enums.PositionEnum import *

speed(0)

pensize(2)
pencolor('purple')
bgcolor('gray')

def drawStar():

    drawCross()
    speed(0)
    # star(Position.topRight)
    # home()
    # setx(150)
    # sety(150)
    # left(-90)
    
    positions = [Position.topRight,Position.topLeft,Position.bottonRight,Position.bottonLeft]
    speed(0)
    for p in positions:
        star(p)
        home()
        setx(150)
        sety(150)
        left(-90)

    drawCross(rotate=True)
   
    # for p in positions:
    star(position=Position.topRight,rotate=True)
    star(position=Position.topLeft,rotate=True,second=True)
    starBotton(Position.bottonRight)
    penup()
    home()
    left(180)
    pendown()
    starBotton(Position.bottonLeft)
    
    # speed(1)
    # star(position=Position.bottonRight,rotate=True,second=True)
        # home()
        # setx(150)
        # sety(150)
        # left(-90)

def drawCross(rotate = False):
    # hideturtle()
   
    if(not rotate):
        
        forward(300)
        penup()
        setx(150)
        sety(150)
        left(-90)
        pendown()
        forward(300)
        return
    
    penup()
    setx(300-41.5)
    sety(150-41.5)
    left(-45)
    pendown()
    forward(300)
    penup()
    
    setx(46)
    sety(150-41.5)
    left(90)

    pendown()
    forward(300)

def starBotton(position):
    x = 1
    if(position == Position.bottonRight):
        x = -1
    speed(0)
    axleX = (33 - 15.12) + 15.12
    axleY = -103.5 - 15.12
    penup()
    sety(-103.5)
    left(220)
    pendown()
    print(123123)
    
    for i in range(0,7):
        if i != 0:
            penup()
            home()
            sety(-103.5)
            setx(33)
            left(45)
            pendown()
             
        catetoAdjascente = ((150 - (21.42*i)))
        catetoOposto = 21.42 + (21.42*i)
        hipotenusa = (sqrt((catetoAdjascente**2)+(catetoOposto**2)))
        print('Cateto oposto: ',catetoOposto)
        print('Cateto adjascente: ',catetoAdjascente)
        print('Hipotenusa',hipotenusa)
        print('='*20,(hipotenusa))
        axleY = axleY + 15.12 
        axleX = axleX + 15.12 
      
        if axleY != -104.5:
            penup()
            sety(axleY)
            setx(axleX )
            pendown()
        left((degrees(asin((catetoOposto/hipotenusa)))+((2.5 if i == 0 else 0) if position == Position.bottonRight else (5 if i ==0 else 0)))*x)
        print('grau',(degrees(atan((catetoOposto/hipotenusa)))))
        forward(hipotenusa)
        if(i == 6):
            break

def star(position,rotate = False,second = False):
    x = 1
    y = 1
    axleX = 258.5
    axleY = 108.5
    if(position == Position.topLeft):
        x = -1
    elif(position == Position.bottonRight):
        y = -1
        x = -1

        left(180)
    elif(position == Position.bottonLeft):
        left(180)
        y = -1
   
    for i in range(0,7):
        penup()
        sety((150 - (41.5 if rotate else 0))*y)
        
           

        if not rotate: 
            setx(150) 
        else:
            if i == 0:
                left(-90 if not second else -37)
          
         
               
                
        # if(rotate):
        #     return
        pendown()
        # if(i == 1):
        #     break

        catetoAdjascente = ((150 - (21.42*i)))*y
        catetoOposto = 21.42 + (21.42*i)
        hipotenusa = (sqrt((catetoAdjascente**2)+(catetoOposto**2)))
        
        # print('Cateto oposto: ',catetoOposto)
        # print('Cateto adjascente: ',catetoAdjascente)
        # print('Hipotenusa',hipotenusa)
        # print('grau: ',degrees(atan(((catetoOposto)/catetoAdjascente))))
        # print('-'*20)

        if(not rotate):
            sety(catetoAdjascente)

        else:
            if((catetoAdjascente != 150 and (catetoAdjascente != (150-41.5) ))):
                # print('Cateto adjascente: ',catetoAdjascente)
               
                axleX = (axleX-15.12)
                axleY = (axleY-15.12)
                penup()
                sety(axleY)
               
                setx(axleX)
                pendown()
           
        
        left((degrees(atan((catetoOposto/hipotenusa)))+(i+4 if i > 2 else i))*x)
       
        forward(hipotenusa)
        left((degrees((atan((catetoOposto/hipotenusa))))*-1)*x)

trocarRazaoTrigonometrica = False
hideturtle()


    # print('!!!!',heading())
# star(position=Position.bottonLeft)

drawStar()

# drawCross()
# drawCross(rotate=True)
mainloop()


