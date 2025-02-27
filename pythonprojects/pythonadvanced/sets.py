"""
sets
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 7 about Sets

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-04
"""

print(set("my name is Tarik and Tarik is my name".split()))

set1 = set([1, 2, 3, 4, 5, 5, 5, 6, 2, 2])
set2 = set([1, 2, 3, 4, 5, 2, 2, 4, 5, 7, 8])

print(set1.intersection(set2))
print(set2.intersection(set1))
print("-----------")

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print("-----------")

print(set1.difference(set2))
print(set2.difference(set1))
print("-----------")

print(set1.union(set2))