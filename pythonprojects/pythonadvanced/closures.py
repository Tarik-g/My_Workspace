"""
closures
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 11 about closures

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-05

Functions:
    outer_function(message): Nested Function that prints a message
    print_msg(number): Nested Function that prints a message
"""

def outer_function(message):
    """
    Nested Function that prints a message to understand closures

    Parameters:
    message (str): message to be printed

    Returns:
    function: inner function

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-05
    """
    def inner_function():
        print(message)
    return inner_function

# Create a closure
my_closure = outer_function("Hello, World!")

# Call the closure
my_closure()  # Output: Hello, World!

#try with and without nonlocal
def print_msg(number):
    """
    Nested Function that prints a message to see how nonlocal works

    Parameters:
    message (str): message to be printed

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-05
    """
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)