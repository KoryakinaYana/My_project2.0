from turtle import *
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
romb(100, 'red')
#Yana - triangle

#Sonya - square
