# Todo add docstrings

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
        if data == self.root_node.get_data():
            raise RootError("The root cant be removed")
        
        node_to_remove = self.search(data)
        if node_to_remove == None:
            return None
        
        
        right = node_to_remove.get_right_child()
        left = node_to_remove.get_left_child()
        parent = node_to_remove.get_parent()

        # leaf node
        if right is None and left is None:
            if node_to_remove.get_data() > parent.get_data():
                parent.set_right_child(None)
            else:
                parent.set_left_child(None)
            node_to_remove.set_parent(None)
        # only left child
        elif right is None:
            node_to_remove.set_parent(None)
            node_to_remove.set_left_child(None)
            parent.set_left_child(left)
            left.set_parent(parent)
        # only right child
        elif left is None:
            node_to_remove.set_parent(None)
            node_to_remove.set_right_child(None)
            parent.set_right_child(right)
            right.set_parent(parent)
        # Two children
        else:
            successor = right
            while successor.get_left_child() is not None:
                successor = successor.get_left_child()

            # If successor is not the immediate right child
            if successor != right:
                successor_parent = successor.get_parent()
                successor_right_child = successor.get_right_child()

                successor_parent.set_left_child(successor_right_child)
                if successor_right_child is not None:
                    successor_right_child.set_parent(successor_parent)

                successor.set_right_child(right)
                right.set_parent(successor)

            if node_to_remove.get_data() > parent.get_data():
                parent.set_right_child(successor)
            else:
                parent.set_left_child(successor)

            successor.set_left_child(left)
            left.set_parent(successor)
            successor.set_parent(parent)
            node_to_remove.set_parent(None)
            node_to_remove.set_right_child(None)
            node_to_remove.set_left_child(None)
        return node_to_remove

    def traversal():
        pass

    def in_order(self, node):
        if node:
            self.in_order(node.get_left_child())
            print(node.get_data(), end=' ')
            self.in_order(node.get_right_child())

    def pre_order(self, node):
        if node:
            print(node.get_data(), end=' ')
            self.pre_order(node.get_left_child())
            self.pre_order(node.get_right_child())

    def post_order(self, node):
        if node:
            self.post_order(node.get_left_child())
            self.post_order(node.get_right_child())
            print(node.get_data(), end=' ')

    def level_order(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.get_data(), end=' ')
            if current_node.get_left_child():
                queue.append(current_node.get_left_child())
            if current_node.get_right_child():
                queue.append(current_node.get_right_child())

    def reverse_in_order(self, node):
        if node:
            self.reverse_in_order(node.get_right_child())
            print(node.get_data(), end=' ')
            self.reverse_in_order(node.get_left_child())


exp_bst = BinarySearchTree(10)

exp_bst.add_node(5)
exp_bst.add_node(1)
exp_bst.add_node(20)
exp_bst.add_node(55)
exp_bst.add_node(34)
exp_bst.add_node(7)
exp_bst.add_node(4)

exp_bst.in_order(exp_bst.root_node)
print("--------------")
exp_bst.pre_order(exp_bst.root_node)
print("--------------")
exp_bst.post_order(exp_bst.root_node)
print("--------------")
exp_bst.reverse_in_order(exp_bst.root_node)
print("--------------")
exp_bst.level_order(exp_bst.root_node)