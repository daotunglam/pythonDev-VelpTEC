from turtle import *
import time

def baum(x):
    if x<5: return
    else:
        print('forward',x)
        forward(x)

        print('left 45')
        left(45)

        print('baum',x/2)
        baum(x/2)

        print('right 90')
        right(90)

        print('baum', x/2)
        baum(x/2)

        print('left 45')
        left(45)

        print('back', x)
        back(x)

    print('return')
    return

speed(1)
left(90)
baum(100)
hideturtle()