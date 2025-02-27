"""
modules_and_packages
============

Python basic Tutorial from https://www.learnpython.org/
Lesson 12 about Modules and Packages

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

from PythonBasics import examplepackage
import functions
from functions import summe
from functions import summe as addieren

#alles importieren mit namespace
from functions import *

print(functions.summe(3,4))
print(summe(3,4))
print(addieren(3,4))

#import PythonBasics.examplepackage.expample_import1
print(examplepackage.example_import1.substract(10, 5))

from PythonBasics.examplepackage import example_import1
print(example_import1.substract(15, 5))

#import sys
#print(sys.path)

#dir(functions)
#help

#sys.path.append('/path/to/your/modules')
#sys.path.append('/another/path')