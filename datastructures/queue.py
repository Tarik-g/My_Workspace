"""
queue
============

Queues are dynamic like list, but when you get an item its the first one

FIFO = first in first out

List based queue is slow, use import deque instead

Use queues when order matters (first item handled first) and for
algorithms like breadth-first search

Dont use queues when random access is needed, high performance is
needed and if its a simple single threaded task

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

# fast queue with import dequeue
from collections import deque

class QueueWithDeque():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self, data):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("Dequeue from an empty queue")

# imported queue
import queue as q

example_queue = q.Queue()
for x in range (5):
    example_queue.put(x)

# slow list queue
class QueueWithList():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self, data):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from an empty queue")