from turtle import *
def sierpinski(x):
    if x < 5: return
    else:
        fd(x) #1
        right(120)
        fd(x)
        right(120)
        fd(x)
        right(120)
        sierpinski(x/2) #2
        fd(x/2)
        sierpinski(x/2) #2
        back(x/2)
        right(60)
        fd(x/2)
        left(60)
        sierpinski(x/2) #2
        right(60)
        back(x/2)
        left(60)
    return
speed(0) #3
left(60)
sierpinski(200)
hideturtle()