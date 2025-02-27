"""
list_comprehensions
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 2 about List Comprehensions

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list = [int(number) for number in numbers if number > 0]
print(new_list)