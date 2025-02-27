"""
classes_and_objects
============

Python basic Tutorial from https://www.learnpython.org/
Lesson 10 about Classes and Objects

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-03

Classes:
    Hund: Class for a dog
"""

class Hund:
    """
    Hund is a dog Class that can bark with the bellen() function

    Attributes:
    name (str): name of the dog
    alter (int): age of the dog

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-03
    """
    def __init__(self, name, alter):
        """
        Constructor that sets the name and age of the dog

        Parameters:
        name (str): name of the dog
        alter (int): age of the dog

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-03
        """
        self.name = name
        self.alter = alter
    
    def bellen(self):
        """
        Function that lets the dog bark by printing

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-03
        """
        print("%s bellt Wuff" % self.name)
    
    def getalter(self):
        """
        Function that returns the age of a dog instance

        Returns:
        int: age of the dog

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-03
        """
        return self.alter


bello = Hund("Bello", 5)
celo = Hund("Celo", 4)
if bello.alter == 5:
    print("yess")

bello.alter = 3
print(bello.alter)
print(celo.alter)
print(bello.getalter())

bello.bellen()