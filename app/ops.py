from .node import Node, Tree


def create_tree(data):
    return Tree(Node(parent=None, left_child=None, right_child=None, data=data))


def create_tree_from_list(data_list):
    t = create_tree(data_list[0])
    for n in data_list[1:]:
        tree_insert(t, n)
    return t


def tree_search(node, data):
    if node is None or node.data == data:
        return node

    if data < node.data:
        return tree_search(node.left_child, data)
    else:
        return tree_search(node.right_child, data)


def tree_minimum(node):
    while node.left_child is not None:
        node = node.left_child
    return node


def tree_maximum(node):
    while node.right_child is not None:
        node = node.right_child
    return node


def tree_successor(node):
    if node.right_child is not None:
        return tree_successor(node.right_child)

    y = node.parent
    while y is not None and node == y.right_child:
        node = y
        y = y.parent

    return y


def tree_insert(tree, data):
    y = None
    x = tree.root
    node = Node(data=data)

    while x is not None:
        y = x
        if node.data < x.data:
            x = x.left_child
        else:
            x = x.right_child

    node.parent = y
    if y is None:
        tree.root = node
    elif node.data < y.data:
        y.left_child = node
    else:
        y.right_child = node


def tree_delete(tree, data):

    node = tree_search(tree.root, data)
    if node is None:
        return

    if node.left_child is None or node.right_child is None:
        y = node
    else:
        y = tree_successor(node)

    if y.left_child is not None:
        x = y.left_child
    else:
        x = y.right_child

    if x is not None:
        x.parent = y.parent

    if y.parent is None:
        tree.root = x
    elif y == y.parent.left_child:
        y.parent.left_child = x
    else:
        y.parent.right_child = x

    if y != node:
        node.data = y.data


def tree_print(tree):
    _print_subtree(tree.root)


def _print_subtree(node):
    if node is not None:
        _print_subtree(node.left_child)
        print(node)
        _print_subtree(node.right_child)
