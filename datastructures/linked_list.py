"""
linked-list
============

Linked lists are ideal for frequently using deletes and insertions and
if the size is dynamic.

Dont use when cache and memory is important and random access is needed

Python normally has no linked lists. You have to implement them or
import them from third parties.

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-11

Classes:
    Node: represents the nodes in a linked list
    LinkedList: linked list using nodes class with basic opertions
"""

class Node():
    """
    Node represents the nodes in a linked list

    Attributes:
    data (obj): data
    next (obj): pointer to the next node

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-11
    """
    def __init__(self, data, next = None):
        """
        Constructor setting data and the next node

        Parameters:
        data (obj): data
        next (obj): pointer to the next node, None by default

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-11
        """
        self.data = data
        self.next = next
    
    def get_data(self):
        """
        Returns the data of a node

        Returns:
        obj: data of a node

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-11
        """
        return self.data

    def set_data(self, data):
        """
        Sets the data of a node

        Parameters:
        data (obj): data to be set

        Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
        1.0.0

        Date:
        2024-08-11
        """
        self.data = data

    def get_next(self):
        """
        Returns the pointer to the next node of a node

        Returns:
        obj: pointer to the next node of a node

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-11
        """
        return self.next

    def set_next(self, next):
        """
        Sets the pointer to the next node of a node

        Parameters:
        next (obj): pointer to the next node of a node to be set

        Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
        1.0.0

        Date:
        2024-08-11
        """
        self.next = next


class LinkedList():
    """
    Linked list using nodes with the basic opertions get_size, find,
    remove and add

    Attributes:
    root (int): root node of the linked list
    size (int): size of the linked list

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-11
    """
    def __init__(self, root = None):
        """
        Constructor setting root and the size to 0

        Parameters:
            root (int): root node of the linked list, default is None

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-11
        """
        self.root = root
        self.size = 0

    def get_size(self):
        """
        Returns the size of the linked list

        Returns:
        int: size of the linked list

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-11
        """
        return self.size
 
    def add(self, data):
        """
        Adds an entry to the linked list

        Parameters:
        data (obj): data to be added to the linked list

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-11
        """
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        """
        Removes an entry from the linked list

        Parameters:
        data (obj): data to removed from the linked list

        Returns:
        bool: if the data could be removed

        Author:
            Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
            1.0.0

        Date:
            2024-08-11
        """
        previous_node = None
        this_node = self.root
        while this_node:
            if this_node.get_data == data:
                if previous_node:
                    # set pointer from previous on to the next node
                    # (skip the removed one)
                    previous_node.set_next(this_node.get_next())
                else:
                    # if its the root than set new root
                    # (skip the removed one which is the root)
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            previous_node = this_node
            this_node = this_node.get_next()
        return False

    def find(self, data):
        """
        Finds an entry from the linked list

        Parameters:
        data (obj): data to be find in the linked list

        Returns:
        obj: either the data or None if it wasnt found

        Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

        Version:
        1.0.0

        Date:
        2024-08-11
        """
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None

example_llist = LinkedList()
example_llist.add(4)

print(example_llist.find(4))