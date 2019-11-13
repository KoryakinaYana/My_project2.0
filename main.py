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
cat()
#Yana - bear
goto(-900,300)
left(45)
forward(150)
right(180)
triangle (150,'black','brown')

#Sonya - ...



