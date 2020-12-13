"""
Not a leetcode problem, but generally useful tree traversal method.
"""


# BFS - Breadth first search. Visit all of a node's children before going to
# the next level.

# Implemented with a queue. We use a Python list because it's easy, but we
# could implement the Queue using a Singly Linked List or Doubly Linked List
# as well if we needed.

# NOTE: The downside to using Python lists for queues is that the delete
# operation takes O(n) time to dequeue. A LL implementation could do so in
# constant time.

# Assuming we're dealing with a binary tree.
def bfs_binary_tree(root):

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


# General graph BFS (a node can have any number of neighbors). BFS Traversal
# is done using a queue.


def bfs_graph(root):

    q = []
    root.visited = True
    q.append(root)

    while q:

        node = q[0]
        del q[0]

        print(f"Now on node: {node}")

        for neighbor in node.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                q.append(neighbor)


# Binary Tree Test
#      a
#    /   \
#   b     c
#  / \   /  \
# d   e f    g

# Order of printing should be:
# a, b, c, d, e, f, g


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

print("\nBinary tree BFS:")
print("-" * 20)
bfs_binary_tree(a)


# Arbitrary graph traversal test
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

print("\n   Graph BFS:")
print("-" * 20)
bfs_graph(a)
