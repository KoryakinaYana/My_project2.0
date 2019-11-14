from turtle import *
from math import sqrt
t = Turtle()
t.screen.setup(1200, 1200)
#Geraschenko Maria - def(romb)
#Koryakina Yana - def(triangle)
#LeontevaSofia - def(square)

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
#Sonya - square
