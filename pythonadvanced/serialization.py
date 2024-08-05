"""
serialization
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 8 about Serialization

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-05

Functions:
    add_employee(salaries_json, name, salary): Adds an Employee with Serialization
"""

import json

#print(json.loads(json_string))
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

import json

#Exercise
# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    """
    Adds an Employee with Serialization

    Parameters:
    salaries_json(dict): salaries of the employees
    name (str): name of the added employee
    salary (int): salary of the added employee

    Returns:
    JSON: updated salary

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-05
    """
    # Add your code here
    salaries = json.loads(salaries_json)
    salaries[name] = salary
    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])