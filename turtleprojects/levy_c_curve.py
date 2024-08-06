"""
levy_c_curve
============

Draws the levy-c curev with turtle

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-06

Functions:
    f_changer(f_combo): swaps F with +F--F+
    instruction_constructor(iteration): returns the instructions for 
      the drawer
    levy_c_curve_drawer(length, order): draws the levy c curve
"""

import time
from turtle import *
import turtle

def f_changer(f_combo):
    """
    Swaps F with +F--F+
    
    Parameters:
    f_combo (str): string to be changed

    Returns:
    string: changed string

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    result = ""
    for char in f_combo:
        if char == '+':
            result += '+'
        elif char == '-':
            result += '-'
        else:
            result += "+F--F+"
    return result

# print(string_changer("F"))
# print(string_changer("+F--F+"))

def instruction_constructor(iteration):
    """
    Recursive Function that returns the instructions for the drawer

    Parameters:
    iteration (int): iteration level

    Returns:
    str: instruction for the drawer

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    if iteration == 0:
        return "F"
    else:
        return f_changer(instruction_constructor(iteration-1))

# print(instruction_constructor(0))
# print(instruction_constructor(1))
# print(instruction_constructor(2))
# print(instruction_constructor(3))


def levy_c_curve_drawer(length, order):
    """
    Draws the levy-c curve

    Parameters:
    length (int): length of a line
    order (int): order of the levy c curve

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    instuctions = instruction_constructor(order)
    for instruction in instuctions:
        if instruction == '+':
            right(45)
        elif instruction == '-':
            left(45)
        else:
            forward(length)

turtle.speed(10)
penup()
backward(100)
pendown()
levy_c_curve_drawer(5, 10)
time.sleep(2)
turtle.Screen().clear()