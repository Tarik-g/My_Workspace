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
    
    def get_parent(self):
        return self.parent

    def add_left_child(self, child):
        if self.left_child is not None:
            self.left_child = child
        raise AlreadyExistsError ("Node already has a left child")

    def add_right_child(self, child):
        if self.right_child is not None:
            self.right_child = child
        raise AlreadyExistsError ("Node already has a right child")

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
                return True
            elif data < current_node.get_data():
                current_node = current_node.get_left_child()
            else:
                current_node = current_node.get_right_child()
        return False
    
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
            previous_node.add_left_child(new_node)
        else:
            previous_node.add_right_child(new_node)
        self.nodes.append(new_node)
        
    
    def remove_node(self, data):
        previous_node = None
        current_node = self.root
        if current_node.get_data == data:
            raise RootError ("The root cant be removed")
        while current_node:
            if current_node.get_data == data:
                
                pass
                # child ändern und parents
            elif data < current_node.get_data():
                previous_node = current_node
                current_node = current_node.get_left_child()
            else:
                previous_node = current_node
                current_node = current_node.get_right_child()
        raise DoesntExistError ("This node doesnt exist")

        # error if the node is not in the tree
        # depends on the tree type (if it has duplicates etc)
        pass

    def traversal():
        # depends on the tree type (if it has duplicates etc)
        pass

    