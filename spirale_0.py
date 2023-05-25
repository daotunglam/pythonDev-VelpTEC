from turtle import *
def spirale(x):
    forward(x)
    right(90)
    spirale(0.9*x)
    return

spirale(200)