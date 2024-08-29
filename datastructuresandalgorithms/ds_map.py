"""
dictionaries
============

Python basic Tutorial from https://www.learnpython.org/
Lesson 11 about dictionaries

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

# maps are dictionaries in Python

# hashing describes the assiggnment of keys to the values

telefonbuch = {}

telefonbuch["tarik"] = 176
telefonbuch["far"] = 190
telefonbuch["mart"] = 154
telefonbuch["rar"] = 134

print(telefonbuch)

for name, nummer in telefonbuch.items():
    print(name, nummer)

for name in telefonbuch.items():
    print(name)

for name in telefonbuch:
    print(name)

telefonbuch = {
    "meh" : 231432,
    "joh" :23742347
}
print(telefonbuch)

del telefonbuch["meh"]
telefonbuch.pop("joh")
print(telefonbuch)