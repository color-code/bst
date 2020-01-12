class Node:
    def __init__(self, parent=None, left_child=None, right_child=None, data=None):
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.data = data

    def __str__(self):
        return f"{self.data}"

class Tree:
    def __init__(self, node):
        self.root = node
