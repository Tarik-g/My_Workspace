"""
regular_expressions
============

Python Advanced Tutorial from https://www.learnpython.org/
Lesson 5 about Regular Expressions

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-04
Functions:
    test_email(your_pattern): tests regular expression
"""

# Example: 
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example

# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    """
    Tests the regular expression

    Parameters:
    your_pattern (str): regular expression

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-04
    """
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
#Lösung kopiert von Website
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
#etwas steht dann @ dann wieder was steht und dann . und dann wieder was steht
test_email(pattern)