# LIFO
"""
Advantages of Stacks
Simple Implementation: Stacks are relatively simple to implement and use.
Efficient Operations: Both push and pop operations are O(1) (constant time) due to their direct access to the end of the list or deque.
Useful for Certain Algorithms: Stacks are essential for algorithms such as depth-first search, expression evaluation, and backtracking.
Function Call Management: The call stack in programming languages manages function calls and returns, which is a stack in itself.
Disadvantages of Stacks
Limited Access: You can only access the top element, which might not be ideal if you need to access elements at arbitrary positions.
Potential for Overflow: If not implemented carefully (especially in languages without dynamic memory management), stacks might suffer from overflow errors if the limit is reached.
Not Ideal for All Scenarios: For applications requiring more flexible access patterns or where elements need to be accessed in various orders, stacks might not be the best choice.
When to Use Stacks
Function Call Management: Managing function calls, recursion, and local variables.
Algorithm Implementation: For algorithms that require backtracking or need to process elements in reverse order.
Undo Mechanisms: Implementing features that allow users to undo previous actions, such as in text editors.
When Not to Use Stacks
Random Access Required: When you need to access elements at arbitrary positions, a stack is not suitable.
Maintaining Order: If you need to maintain or process elements in the order they were added or require sorted order, other data structures like queues or lists might be more appropriate.
"""

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