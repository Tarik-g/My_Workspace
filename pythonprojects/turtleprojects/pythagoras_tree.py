"""
pythagoras_tree
============

Draws a pythagoras tree with turtle

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-06

Functions:
    pythagoras_tree_drawer(hypotenuse_or_side): draws a pythagoras tree
    square_drawer(side): draws a square and a right triangle on top
    triangle_drawer(a, b, c): draws a right triangle and 2 squares on
      the kathete sides
"""

import math
from turtle import *
import turtle

def pythagoras_tree_drawer(hypotenuse_or_side):
    """
    Uses the square_drawer Function to draw a pythagoras tree

    Parameters:
    hypotenuse_or_side (int): length of the side/hypotenuse

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    square_drawer(hypotenuse_or_side)

def square_drawer(side):
    """
    Recursive function that draws a square and a right triangle on top

    Parameters:
    side (int): length of the side

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
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
    """
    Recursive function that draws a right triangle and 2 squares on the
    kathete sides

    Parameters:
    a (int): kathete a
    b (int): kathete b
    c (int): hypotenuse a

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
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

turtle.speed(10)
penup()
right(90)
forward(200)
left(90)
pendown()
pythagoras_tree_drawer(100)