"""
Script Title
============

FIFO

list based queue is slow

When to Use Queues
Task Scheduling: When you need to manage tasks or jobs that should be processed in the order they are received.
Breadth-First Search: In algorithms like BFS, where nodes are explored level by level.
Producer-Consumer Problems: When you have multiple producers and consumers and need to manage their interactions efficiently.
Event Handling: In event-driven programming, where events need to be processed in the order they occur.

When Not to Use Queues
Random Accesse
High-Performance Needs.
Single-Threaded Simple Tasks

Brief summary

Extended Description, purpose, other datails

Dependencies:
    pandas >= 1.3.0

Usage:
    python data_processing.py --input_dir /path/to/raw_data --output_dir /path/to/clean_data

Parameters:
    input_dir (str): The directory containing raw data files.
    output_dir (str): The directory where cleaned data files will be
        saved.

Returns:
    Saves cleaned data files to the specified output directory.

Error Handling:
    Raises ValueError if input directory does not exist or is empty.

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-17

License:
    MIT License

References:
    Data Wrangling with Pandas: https://pandas.pydata.org/docs/

Change Log:
    Version 1.2.0: Added normalization step.
    Version 1.1.0: Improved handling of missing values.
    Version 1.0.0 (2024-06-01):
        Initial release with basic functionality for processing strings.

Contact Information:
    For issues, contact Tarik Gökmen at tarikgokmen1999@gmail.com or
    visit https://github.com/Tarik-g

Known Issues/ Limitations:
    Currently does not support multi-threaded processing.

Notes:
    Ensure that the raw data files are in CSV format and follow the
    expected schema.
Note:
    This is a private script and is intended for internal use only.
    Should not be used directly by external code.
Note:
    This script contains some private classes or functions intended for
    internaluse only. These functions or classes are prefixed with an
    underscore (_) and should not be used directly in external code.
"""

"""
    haracteristics of Queues
FIFO Ordering: The first element added to the queue is the first one to be removed. This is the defining characteristic of a queue.
Dynamic Sizing: Queues can grow and shrink dynamically as elements are added or removed.
Operations: Typically, queues support at least two main operations:
Enqueue: Add an element to the end of the queue.
Dequeue: Remove an element from the front of the queue.
"""

# fast queue with import dequeue
from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self, data):
        self.queue.popleft()

# imported queue
import queue as q

example_queue = q.Queue()
for x in range (5):
    example_queue.put(x)

# slow list queue
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self, data):
        self.queue.pop(0)