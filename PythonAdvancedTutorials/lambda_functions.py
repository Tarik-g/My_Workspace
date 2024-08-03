"""
lambda_functions
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 3 about Lambda Functions

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

list = [2,4,7,3,14,19]
for i in list:
    is_odd = lambda number : bool(number%2)
    print(is_odd(i))

#solution from the website:
l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))