"""
decorators
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 12 about Decorators

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-05
    
Functions:
    repeater(old_function): function Decorator that repeats twice
    multiply(num1, num2): multiplies two numbers and prints result
"""

def repeater(old_function):
    """
    Function Decorator that repeats the old function twice

    Parameters:
    old_function (func): old funtion thats decorated

    Returns:
    func: decorated function

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-05
    """
    def new_function(*args, **kwds):
        old_function(*args, **kwds) # we run the old function twice
        old_function(*args, **kwds)
    # return the new_function, or it wouldn't reassign it to the value
    return new_function

def multiply(num1, num2):
    """
    Multiplies two numbers and prints result

    Parameters:
    num1 (int): first number
    num2 (int): second number

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-05
    """
    print(num1 * num2)

multiply_rep = repeater(multiply)
multiply_rep(2, 2)

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 3)