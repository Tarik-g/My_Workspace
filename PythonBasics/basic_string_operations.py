"""
basic_string_operations
============

Python basic Tutorial from https://www.learnpython.org/
Lesson 6 about Basic String Operations

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

name = "tariktariktarik"
print(len(name))
print(name.index("a"))
print(name.count("a"))
print(name[1:3])
print(name[3])
print(name[:3])
print(name[1:])
print(name[:])
print(name[-3:-1])
print(name[1:9:2])
print(name[::-1])

astring = "Heloworld!"
print(astring[3:8:2])
print(astring.upper())
print(astring.lower())
print(name.startswith("tar"))
print(name.endswith("lol"))
print(name.split("t"))