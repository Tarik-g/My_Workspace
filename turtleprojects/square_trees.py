"""
square_trees
============

Draws 2 diffrent square trees with turtle

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-06

Functions:
    square_tree_v1(side): draws the square tree v1
    square_tree_v2(side): draws the square tree v2
"""

import time
from turtle import *
import turtle

def square_tree_v1(side):
    """
    Recursive function that draws the square tree v1

    Parameters:
    side (int): side length

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    if side < 10:
        return
    for i in range (4):
        forward(side)
        right(90)
        square_tree_v1(side/2)
        left(180)

turtle.speed(10)
penup()
backward(75)
right(90)
forward(75)
left(90)
pendown()
square_tree_v1(150)

def square_tree_v2(side):
    """
    Recursive function that draws the square tree v2

    Parameters:
    side (int): side length

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
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

time.sleep(2)
turtle.Screen().clear()
turtle.speed(10)
penup()
left(90)
backward(150)
pendown()
square_tree_v2(150)
time.sleep(2)