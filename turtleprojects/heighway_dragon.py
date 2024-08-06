"""
heighway_dragon
============

Draws the heighway dragon (dragon curve) with turtle

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-06

Functions:
    string_changer(rl_combo): swaps L and R and reverses
    iteration_finder(iteration): returns the instrcution
    heighway_dragon_drawer(length, order): draws the heigway dragon
"""

import time
from turtle import *
import turtle

def string_changer(rl_combo):
    """
    Swaps L and R and reverses

    Parameters:
    rl_combo (str): string with R and L

    Returns:
    string: swaped and reversed string

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    result = ""
    for char in rl_combo:
        if char == 'R':
            result += 'L'
        else:
            result += 'R'
    return result[::-1]

# print(string_changer("RRL"))
# print(string_changer("RRLRRLL"))

def iteration_finder(iteration):
    """
    Recursive Function that returns the instrcution

    Parameters:
    iteration (int): the iteration level

    Returns:
    str: returns the instrcution

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    if iteration == 1:
        return "R"
    else:
        return iteration_finder(iteration-1) + "R" + string_changer(iteration_finder(iteration-1))

# print(iteration_finder(1))
# print(iteration_finder(2))
# print(iteration_finder(3))
# print(iteration_finder(4))

def heighway_dragon_drawer(length, order):
    """
    Draws the heigway dragon

    Parameters:
    length (int): length of the lines
    order (int): order of the heighway dragon

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-06
    """
    forward(length)
    instructions = iteration_finder(order)
    for instruction in instructions:
        if instruction == "R":
            right(90)
            forward(length)
        else:
            left(90)
            forward(length)

turtle.speed(10)
penup()
backward(100)
left(90)
pendown()
heighway_dragon_drawer(5, 15)
time.sleep(2)
turtle.Screen().clear()