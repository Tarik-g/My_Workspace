"""
generators
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 1 about Generators

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03

Functions:
    drei_zufalls_zahlen(): Generator that yields 3 random numbers
    fib(): Generator that yield Fibonacci Numbers
"""

import random

def drei_zufalls_zahlen():
    """
    Generator that yields three random numbers

    Yields:
    int: from 1 to 100
    int: from 1 to 1000

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    for i in range(2):
        yield random.randint(1,100)
    
    yield random.randint(1,1000)

for zufalls_zahl in drei_zufalls_zahlen():
    print("Und die nächste Zahl %d" % zufalls_zahl)

def fib():
    """
    Generator that return Fibonacci numbers

    Returns:
    int: Fibonacci Number

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    a,b = 1,1
    while 1:
        yield a
        a,b = b, a+b

import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break