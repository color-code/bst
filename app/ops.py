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


def tree_minimum(x):
    while x.left_child is not None:
        x = x.left_child

    return x


def tree_maximum(x):
    while x.right_child is not None:
        x = x.right_child

    return x


def tree_successor(x):
    if x.right_child is not None:
        return tree_minimum(x.right_child)
    else:
        y = x.parent
        while y is not None and x == y.right_child:
            x = y
            y = y.parent

        return y


def tree_insert(tree, data):
    y = None
    x = tree.root
    z = Node(data=data)

    while x is not None:
        y = x
        if z.data < x.data:
            x = x.left_child
        else:
            x = x.right_child

    z.parent = y
    if y is None:
        tree.root = z
    elif z.data < y.data:
        y.left_child = z
    else:
        y.right_child = z


def tree_delete(tree, data):

    z = tree_search(tree.root, data)

    if z is None:
        raise LookupError(f"Failed to find {data}")

    if z.left_child is None or z.right_child is None:
        y = z
    else:
        y = tree_successor(z)

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

    if y != z:
        z.data = y.data

    return y


def tree_print(tree):
    _print_subtree(tree.root)


def _print_subtree(node):
    if node is not None:
        _print_subtree(node.left_child)
        print(node)
        _print_subtree(node.right_child)


def tree_to_list(tree):
    return _tree_to_list(tree.root, [])


def _tree_to_list(node, tree_nodes):
    if node is not None:
        _tree_to_list(node.left_child, tree_nodes)
        tree_nodes.append(node.data)
        _tree_to_list(node.right_child, tree_nodes)

    return tree_nodes
