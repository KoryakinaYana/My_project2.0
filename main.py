from turtle import *
from math import sqrt
#Geraschenko Maria - def(romb)
#Koryakina Yana - def(triangle)
#LeontyevaSofia - def(square)

#Maria - romb
def romb(x,color1,fillcolor1):
    down()
    color(color1)
    begin_fill()
    fillcolor(fillcolor1)
    for _ in range (2):
        forward(x)
        right(135)
        forward(x)
        right(45)
    end_fill()
    up()
#Yana - triangle
def triangle (x,color2,fillcolor2):
    down()
    color(color2)
    begin_fill()
    fillcolor(fillcolor2)
    forward (x)
    left (90)
    forward (x)
    left (135)
    forward (sqrt(2*x**2))
    end_fill()
    up()
#Sonya - square
def square (x,color3,fillcolor3):
    down()
    color(color3)
    begin_fill()
    fillcolor(fillcolor3)
    for _ in range (4):
        forward (x)
        left (90)
    end_fill()
    up()
#Yana - cat
up()
goto(-800, -400)
def cat():
    triangle (150,'black','red')
    left(135)
    forward(200)
    left(180)
    romb(100,'black','red')
    forward(50)
    right(90)
    forward(150)
    left(45)
    forward(150)
    left(135)
    forward (sqrt(2*150**2))
    left(135)
    triangle(150,'black','red')
    left(180)
    forward (sqrt(2*150**2))
    left(135)
    triangle(100,'black','red')
    left(135)
    forward(30)
    right(180)
    square(80,'black','red')
    forward(80)
    left(90)
    forward(80)
    right(90)
    forward(80)
    left(180)
    triangle(80,'black','red')
    left(135)
    forward(160)
    right(180)
    triangle(80,'black','red')
    left(90)
#Yana - bear
def bear():
    goto(-900,300)
    left(45)
    forward(150)
    right(180)
    triangle (150,'black','brown')
    left(180)
    forward (sqrt(2*150**2))
    right(135)
    forward(50)
    left(180)
    right(45)
    triangle (80,'black','brown')
    forward(100)
    right(90)
    forward(150)
    right(45)
    forward(150)
    left(180)
    triangle (150,'black','brown')
    left(180)
    forward (sqrt(2*100**2))
    left(135)
    triangle (100,'black','brown')
    left(135)
    forward(130)
    right(135)
    forward(75)
    right(90)
    romb(75,'black','brown')
    forward(75)
    right(135)
    forward(75)
    left(90)
    forward(30)
    right(90)
    square(70,'black','brown')
    forward(70)
    left(90)
    forward(70)
    left(180)
    triangle (70,'black','brown')
    right(135)
#Sonya - swan
up()
goto(100, 50)
def swan():
    down()
    triangle(30, 'black', 'yellow')
    left(135)
    forward(30)
    left(90)
    forward(30)
    right(135)
    romb(40, 'black', 'yellow')
    back(40)
    left(135)
    square(40, 'black', 'yellow')
    back(40)
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(180)
    triangle(40, 'black', 'yellow')
    right(135)
    forward(40)
    right(90)
    forward(40)
    back(60)
    triangle(60, 'black', 'yellow')
    left(180)
    triangle(85, 'black', 'yellow')
    left(180)
    triangle(85, 'black', 'yellow')
    left(180)
    forward(100)



