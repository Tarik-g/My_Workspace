"""
stack
============

Stacks are dynamic like list, but when you get an item its the last one

LIFO = last in first out

List based stacks are fast.

Use queues when order matters (last item handled first) and for
algorithms.

Dont use queues when random access is needed.

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-20

License:
    MIT License

Change Log:
    Version 1.0.0 (2024-08-20):
        Initial release.

Contact Information:
    For issues, contact Tarik Gökmen at tarikgokmen1999@gmail.com or
    visit https://github.com/Tarik-g
"""

# following have no docstrings

# list based stack is fast because end of list allways
class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from an empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len (self.stack) == 0