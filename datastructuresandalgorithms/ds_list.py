"""
list
============

Lists in python are dynamic arrays that are easy to use, felxible,
dynamic, good for mixed data and indexing.

Dont use when large data is given. It can also be bad for fixed type
operations and can be slow.

There are several in built functions that are useful like map, filter,
reduce and so on.

List comprehensions are powerful one liners.

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-017
"""


meine_liste = []
meine_liste.append(1)
meine_liste.append(2)
meine_liste.append(3)

print(meine_liste[0])

for x in meine_liste:
    print(x)

# list comprehension
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list = [int(number) for number in numbers if number > 0]
print(new_list)

# map, filter, reduce
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