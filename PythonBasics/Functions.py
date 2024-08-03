"""
functions
============

Python basic Tutorial from https://www.learnpython.org/
Lesson 9 about Functions

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03

Functions:
    bsp_funktion(): prints "maschine" and returns 7
    gruss(name, gruss): greets a person
    summe(a, b): returns the sum of two numbers
"""

def bsp_funktion():
    """
    Prints "maschine" and returns 7

    Returns:
    int: 7

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    print ("maschine")
    return 3+4

def gruss(name, gruss):
    """
    Greets someone with a name and a special greeting

    Parameters:
    name (str): name of the person greeted
    gruss (str): special greeting

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    print("Hallo %s , ich wünsche dir %s" %(name, gruss))

def summe(a,b):
    """
    Returns the sum of two numbers

    Parameters:
    a (int): first number of the addition
    b (int): second number of the addition

    Returns:
    int: sum of a and b

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    return a +b

if __name__ == "__main__":
    gruss("tarik", "schöne Ferien")
    print(summe(5, 4))