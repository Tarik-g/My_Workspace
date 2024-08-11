"""
ds_arrays
============

Arrays are ideal for fast access by index and if the size is known and
fix.

Dont use when frequent delete and insertions are needed and size is
dynamic

Python normally uses lists instead of arrays but with the array module
you can use arrays

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-11
"""

import array as ar

example_array_of_integers = ar.array('i',[1, 2, 3, 4, 5])

print(example_array_of_integers)
print(example_array_of_integers[4])