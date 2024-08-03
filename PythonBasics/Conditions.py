"""
conditions
============

Python basic Tutorial from https://www.learnpython.org/
Lesson 7 about Conditions

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03
"""

x = 4
print(x!=3)
print(x==4)
print(x>3)

if x ==5 and x>1:
    print("yessir")
elif x ==4:
    print("foa")
else:
    print("no")

if x ==4 or x>1:
    print("yessir")

if x in [4, 3]:
    print("Yeahhh")

if x is 4:
    print("ya")

liste1 = [1,2,3]
liste2 = [1,2,3]
print(liste1 == liste2) 
print(liste1 is liste2) 

print(not False)

if x ==4:
    pass