"""
multiple_function_arguments
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 4 about Multiple Function Arguments

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03

Functions:
    foo(a, b, c, *rest): return amount of extra Arguments
    bar(a, b, c,**options): returns true when keyword magicnumber is 7
"""

def foo(a, b, c, *rest):
    """
    The foo function must return the amount of extra arguments received.

    Parameters:
    a (int): Argument 1
    b (int): Argument 2
    c (int): Argument 3
    *rest (int): extra Arguments

    Returns:
    int: amount of extra arguments received

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    count = 0
    for number in rest:
        count += 1
    return count

def bar(a, b, c,**options):
    """
    The bar must return True if the argument with the keyword
    magicnumber is worth 7, and False otherwise

    Parameters:
    a (int): Argument 1
    b (int): Argument 2
    c (int): Argument 3
    **options: keyword

    Returns:
    bool: True when magicnumber is 7

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    if options.get("magicnumber") == 7:
        return True
    else:
        return False
    
#solution from website:
#def foo(a, b, c, *args):
    #return len(args)

#def bar(a, b, c, **kwargs):
    #return kwargs["magicnumber"] == 7

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")