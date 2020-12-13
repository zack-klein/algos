"""
This module just some basic data structures.
"""

# Binary Tree
#      a
#    /   \
#   b     c
#  / \   /  \
# d   e f    g


class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.visited = False

    def __repr__(self):
        return f"Node({self.val})"


g = BinaryTreeNode("g")
f = BinaryTreeNode("f")
c = BinaryTreeNode("c")
c.left = f
c.right = g

e = BinaryTreeNode("e")
d = BinaryTreeNode("d")
b = BinaryTreeNode("b")
b.left = d
b.right = e

a = BinaryTreeNode("a")
a.left = b
a.right = c

binary_tree = a


# Arbitrary graph
#   b - e   g       j
#  /       /       /
# a - c - f - h - i - k
#  \               \
#   d               l


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        self.visited = False

    def __repr__(self):
        return f"Node({self.val})"


a = GraphNode("a")
b = GraphNode("b")
c = GraphNode("c")
d = GraphNode("d")
e = GraphNode("e")
f = GraphNode("f")
g = GraphNode("g")
h = GraphNode("h")
i = GraphNode("i")
j = GraphNode("j")
k = GraphNode("k")
l = GraphNode("l")  # noqa

i.neighbors += [j, k, l]
h.neighbors.append(i)
f.neighbors += [g, h]
c.neighbors.append(f)
b.neighbors.append(e)
a.neighbors += [b, c, d]

graph = a
