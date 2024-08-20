"""
ds_basic_tree
============

Trees are hierarchial data representation

Use for efficient seraching, sorting and traversal and decision making.

Dont use when the data is linear, memory is important and operations
are mostly sequential.  

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

# following have no or some docstrings

class Node():
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.children = []
    
    def add_child_node(self, child):
        self.children.append(child)

class BasicTree():
    def __init__(self, root_data):
        self.root_node = Node(root_data, None)
        self.nodes = [self.root_node]
    
    def add_node(self, data, parent):
        # parent not in the tree error
        new_node = Node(data, parent)
        self.nodes.append(new_node)
        parent.add_child_node(new_node)
    
    def remove_node(self, data):
        # error if the node is not in the tree
        # depends on the tree type (if it has duplicates etc)
        pass

    def traversal():
        # depends on the tree type (if it has duplicates etc)
        pass

    def search():
        # depends on the tree type (if it has duplicates etc)
        pass