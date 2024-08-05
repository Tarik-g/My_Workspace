import math
from turtle import *
import turtle

turtle.speed(10)

def square_tree_v1(side):
    if side < 10:
        return
    for i in range (4):
        forward(side)
        right(90)
        square_tree_v1(side/2)
        left(180)

#square_tree_v1(150)

def square_tree_v2(side):
    right(90)
    forward(side/2)

    left(90)
    forward(side)
    right(45)
    if side > 10:
        square_tree_v2(side/2)
    left(135)
    forward(side)
    right(45)
    if side > 10:
        square_tree_v2(side/2)
    left(135)
    forward(side)
    left(90)
    forward(side/2)
    left(90)

# penup()
# forward(150/2)
# left(90)
# pendown()
# square_tree_v2(150)

def square_tree_v3(side):
    pass



penup()
forward(150/2)
left(90)
pendown()
square_tree_v3(150)