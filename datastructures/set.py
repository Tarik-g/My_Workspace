"""
set
============

Sets are like lists but unordered, mutable, iterable and allow only
unique elements.

Indexing is not possible.

Use to remove duplicates, for membership testing, to use mathematical
operations.

Dont use when order matters, element mutability is needed or you need
key-value pairing.

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-17

License:
    MIT License

Change Log:
    Version 1.0.0 (2024-08-17):
        Initial release

Contact Information:
    For issues, contact Tarik Gökmen at tarikgokmen1999@gmail.com or
    visit https://github.com/Tarik-g
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