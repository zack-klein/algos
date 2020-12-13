"""
Not a leetcode problem, but generally useful tree traversal method.
"""


# BFS - Breadth first search. Visit all of a node's children before going to
# the next level.

# Implemented with a queue. We use a Python list because it's easy, but we
# could implement the Queue using a Singly Linked List or Doubly Linked List
# as well if we needed.

# Assuming we're dealing with a binary tree.
def bfs(root):

    q = []
    root.visited = True
    q.append(root)  # Append == enqueue

    while q:

        # Retrieving with q[0] and del[0] == dequeue
        node = q[0]
        del q[0]

        print(f"Now on node: {node.val}")

        if node.left:
            if not node.left.visited:
                node.left.visited = True
                q.append(node.left)

        if node.right:
            if not node.right.visited:
                node.right.visited = True
                q.append(node.right)


# Tests
#      a
#    /   \
#   b     c
#  / \   /  \
# d   e f    g

# Order of printing should be:
# a, b, c, d, e, f, g


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.visited = False

    def __repr__(self):
        return f"Node({self.val})"


g = Node("g")
f = Node("f")
c = Node("c")
c.left = f
c.right = g

e = Node("e")
d = Node("d")
b = Node("b")
b.left = d
b.right = e

a = Node("a")
a.left = b
a.right = c

bfs(a)
