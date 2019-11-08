from turtle import *
from math import sqrt
#Geraschenko Maria - def(romb)
#Koryakina Yana - def(triangle)
#LeontevaSofia - def(square)

#Maria - romb

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
