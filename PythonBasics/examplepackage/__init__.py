"""
examplepackage
=============

Python basic Tutorial from https://www.learnpython.org/
Part of lesson 12 about Modules and Packages

Notes:
    This package contains some private modules intended for internal
    use only.
    These modules are prefixed with an underscore (_) and should not
    be used directly in external code.

Modules:
    example_import1: contains a subtraction Function
    example_import2: contains a Function that return "Function 2"

Author:
    Tarik Gökmen (tarikgokmen1999@.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

from .example_import1 import substract
from .example_import2 import function2

__all__ = [ 'substract', 'function2']

# Only expose function1 and function2
# _example_import3 is not included in __all__, so it remains internal