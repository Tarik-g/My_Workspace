"""
partial_functions
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 9 about Partial Functions

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-05

Functions:
    func(u, v, w, x): Calculates u*4 + v*3 + w*2 + x
"""

from functools import partial

#Following is the exercise, function provided:
def func(u, v, w, x):
    """
    Calculates u*4 + v*3 + w*2 + x

    Parameters:
    u (int): first number
    v (int): second number
    w (int): third number
    x (int): fourth number

    Returns:
    int: result

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-05
    """
    return u*4 + v*3 + w*2 + x

#Enter your code here to create and print with your partial function
new = partial(func,5,5,5)
print(new(15))