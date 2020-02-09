# Binary Search Trees Code
Python implementation of Binary Search Tree code from "Introduction To Algorithms"

This is the code for the presentations on Binary Search Trees in January/February 2020.

# Usage
This code is really intended to be used interactively. For example, I loaded it into [PyCharm](https://www.jetbrains.com/pycharm/),
launched the Python console and then would use it as follows (the '>>>' is the Python REPL prompt):

```python
>>> from app.ops import *

>>> t1 = create_tree_from_list([15, 5, 16, 3, 12, 20, 10, 13, 18, 23, 6, 7])
>>> tree_print(t1)
3
5
6
7
10
12
13
15
16
18
20
23
>>> tree_delete(t1, 5)
...
```

## Supported Functions
If you look at `ops.py`, you'll see that I've implemented the basic functions to create trees, search them, print them, as well
as adding and deleting new nodes in the tree.

# CAVEAT EMPTOR
There is currently a bug in `master` that causes `tree_delete` not to work in certain circumstances. The example above,
`tree_delete(t1, 5) demonstrates this bug.

I encourage people to fork & submit PR's to fix this bug. If you're really stumped, I will be publishing a fix for it
soon. :)
