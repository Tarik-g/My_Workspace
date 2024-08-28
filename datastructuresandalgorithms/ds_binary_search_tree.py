class AlreadyExistsError(Exception):
    pass

class DoesntExistError(Exception):
    pass

class RootError(Exception):
    pass

class Node():
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def get_data(self):
        return self.data
    
    def set_parent(self,parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_left_child(self, child):
        self.left_child = child

    def set_right_child(self, child):
        self.right_child = child

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
        

class BinarySearchTree():
    def __init__(self, root_data):
        self.root_node = Node(root_data, None)
        self.nodes = [self.root_node]
    
    def search(self, data):
        current_node = self.root_node
        while current_node:
            if data == current_node.get_data():
                return current_node
            elif data < current_node.get_data():
                current_node = current_node.get_left_child()
            else:
                current_node = current_node.get_right_child()
        return None
    
    def add_node(self, data):
        previous_node = None
        current_node = self.root_node
        while current_node:
            if data == current_node.get_data():
                raise AlreadyExistsError ("This node already exists")
            elif data < current_node.get_data():
                previous_node = current_node
                current_node = current_node.get_left_child()
            else:
                previous_node = current_node
                current_node = current_node.get_right_child()
        new_node = Node(data, previous_node)
        if data < previous_node.get_data():
            previous_node.set_left_child(new_node)
        else:
            previous_node.set_right_child(new_node)
        self.nodes.append(new_node)
        
    def remove_node(self, data):
        current_node = self.root_node
        parent = None

        if current_node is None:
            raise ValueError("The tree is empty")

        if current_node.get_data() == data:
            raise RootError("The root can't be removed")

        while current_node:
            if data == current_node.get_data():
                left_child = current_node.get_left_child()
                right_child = current_node.get_right_child()

                # Case 1: Node has two children
                if left_child and right_child:
                    parent.set_left_child(left_child)
                    parent.set_right_child(right_child)
                    left_child.set_parent(parent)
                    right_child.set_parent(parent)

                # Case 2: Node has only one child (left)
                elif left_child:
                    if parent.get_left_child() == current_node:
                        parent.set_left_child(left_child)
                    else:
                        parent.set_right_child(left_child)
                    left_child.set_parent(parent)

                # Case 3: Node has only one child (right)
                elif right_child:
                    if parent.get_left_child() == current_node:
                        parent.set_left_child(right_child)
                    else:
                        parent.set_right_child(right_child)
                    right_child.set_parent(parent)

                # Case 4: Node has no children
                else:
                    if parent.get_left_child() == current_node:
                        parent.set_left_child(None)
                    else:
                        parent.set_right_child(None)

                return

            # Update parent and current node pointers
            parent = current_node
            if data < current_node.get_data():
                current_node = current_node.get_left_child()
            else:
                current_node = current_node.get_right_child()

        raise ValueError("Node with data not found")

        

    def traversal():
        # depends on the tree type (if it has duplicates etc)
        pass

    