"""
variables_and_types
============

Python basic Tutorial from https://www.learnpython.org/
Lesson 2 about Variables and Types

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

x = int(input("Enter a number: "))
print("You have entered: % d" % x)

number = 4
print(number)

kommazahl = 5.0
print(kommazahl)
kommazahl = float(5)
print(kommazahl)

wort = "test"
print(wort)
wort = 'test'
print(wort)

print(kommazahl + kommazahl)
print(wort + wort)

a,b = 2,3
print(a, b)