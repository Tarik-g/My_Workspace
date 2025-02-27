"""
map_filter_reduce
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 13 about Map, Filter and Reduce

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-05
"""

namen = ["tee", "joo"]
print(list(map(str.upper, namen)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
print(list(zip(my_strings, my_numbers)))

print(list(filter(lambda x : (x >2), my_numbers)))

from functools import reduce
print(reduce(lambda a, b : (a+b), my_numbers))
print(reduce(lambda a, b : (a+b), my_numbers, 10))

#Exercise:
# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print(list(map(lambda a : (round((a**2),3)), my_floats)))

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print(list(filter(lambda name : (len(name) < 8), my_names)))

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
print(reduce(lambda x,y : (x*y), my_numbers))

# Fix all three respectively.
map_result = list(map(lambda x: (round((x**2),3)), my_floats))
filter_result = list(filter(lambda name: len(name) < 8, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)