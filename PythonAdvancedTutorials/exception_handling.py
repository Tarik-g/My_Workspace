"""
exception_handling
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 6 about Exception Handling

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-04

Functions:
    get_last_name(): returns last name of an actor
"""

#Exercise
# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name():
    """
    Returns last name of an actor

    Returns:
    str: last name of an actor

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-04
    """
    return actor["name"].split()[1]

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())


#some Exception:
#print(a)
#error a not defined

#catched
try:
    5/0
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
finally:
    print("always executed")

try:
    5/0
except (NameError,ZeroDivisionError):
    print("divided by Zero!")

#catched
try:
    3/2
    try:
        5/0
    except ZeroDivisionError:
        print("divided by Zero!")
except NameError:
    print("Wrong name")

#catched
try:
    3/2
    try:
        5/0
    except NameError:
        print("Wrong name")
except ZeroDivisionError:
        print("divided by Zero!")

try:
    5/0
except ZeroDivisionError as err:
    raise BaseException("demonstration") from err

#raise normaly used in Functions or to chain Exceptions
y = 0
if y == 0:
    raise ZeroDivisionError("Cannot divide by zero")
try:
    5 / y
except ValueError as err:
    print("An error occurred: ", err)

#not catched
try:
    5/0
except NameError:
    print("divided by Zero!")