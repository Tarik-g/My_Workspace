import math
from turtle import *
import turtle

turtle.speed(10)

def pythagoras_tree_drawer(hypotenuse_or_side):
    square_drawer(hypotenuse_or_side)

def square_drawer(side):
    if side < 10:
        return
    forward(side)
    left(90)

    forward(side)
    left(90)

    forward(side)
    triangle_drawer((side * math.sin(math.radians(36.87))), (side * math.sin(math.radians(53.13))), (side))

    left(90)
    forward(side)
    left(90)

def triangle_drawer(a, b, c):
    right(180)

    forward(c)
    left(90 + 90 - 53.13 )
    forward (a)

    right(180)
    if a > 20:
        square_drawer(a)
    right(180)

    left(90)
    forward(b)
    right(180)
    if b > 20:
        square_drawer(b)
    right(180)

    left(90 + 90 - 36.87)
    right(180)

pythagoras_tree_drawer(100)