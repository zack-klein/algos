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


# Tests
# Order of printing should be:
# a, b, c, d, e, f, g
# For both
from tests.trees import binary_tree, graph  # noqa

print("\nBinary tree BFS:")
print("-" * 20)
bfs_binary_tree(binary_tree)


print("\nGraph BFS:")
print("-" * 20)
bfs_graph(graph)
