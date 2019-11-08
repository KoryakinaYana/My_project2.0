from turtle import *
from math import sqrt
#Geraschenko Maria - def(romb)
#Koryakina Yana - def(triangle)
#LeontyevaSofia - def(square)

#Maria - romb
def romb(x, color1):
    down()
    color(color1)
    begin_fill()
    for _ in range (2):
        forward(x)
        right(135)
        forward(x)
        right(45)
    end_fill()
    up()
    mainloop()
romb(100, 'red')
#Yana - triangle
def triangle (x,color2):
    fillcolor(color2)
    begin_fill()
    color(color2)
    forward (x)
    left (90)
    forward (x)
    left (135)
    forward (sqrt(2*x**2))
    end_fill()
    mainloop()
triangle(100, 'green')
#Sonya - square
def square (x, color3):
    fillcolor(color3)
    begin_fill()
    color(color3)
    for _ in range (4):
        forward (x)
        left (90)
    end_fill()
    mainloop()
square(100, 'blue')


