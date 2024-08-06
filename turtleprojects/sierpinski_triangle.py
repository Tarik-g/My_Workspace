"""
sierpinski_triangle
============

Draws the sierpinski triangle with turtle

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-06

Functions:
    sierpinski_triangle_drawer (side_length): draws the sierpinski
      triangle
"""

import time
from turtle import *
import turtle

def sierpinski_triangle_drawer (side_length):
    """
    Recursive function that draws the sierpinski triangle

    Parameters:
    side_length (int): side of the triangle

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    for i in range (3):
        if side_length > 20:
            sierpinski_triangle_drawer(side_length/2)
        forward(side_length)
        left(120)
    
turtle.speed(10)
penup()
backward(100)
right(90)
forward(100)
left(90)
pendown()
sierpinski_triangle_drawer(200)
time.sleep(2)