"""
Just some practice with Depth-First-Search.
"""


# It's really remarkable, we can take basically the exact same code as here:
# https://github.com/zack-klein/algos/blob/7cf6b6212866cff832a44dbb7c5cb2aaa30bd5dd/bfs.py
# (implements a BFS using a queue), switch the data structure from a Queue to a
# Stack, and we have a depth first search instead of a breadth first search!

# I swap the order of the node processing here to process the nodes from left
# to right, but it doesn't really matter, that's just my personal preference.
def iterative_dfs_binary_tree(root):

    stack = []
    root.visited = True
    stack.append(root)

    val = ""

    while stack:

        node = stack.pop()

        val += node.val

        if node.right:
            if not node.right.visited:
                node.right.visited = True
                stack.append(node.right)

        if node.left:
            if not node.left.visited:
                node.left.visited = True
                stack.append(node.left)

    return val


# Using the stack recursively is so clean!
def recursive_dfs_binary_tree(node):
    if not node:
        return ""
    else:
        L = recursive_dfs_binary_tree(node.left)
        R = recursive_dfs_binary_tree(node.right)
        return node.val + L + R


# Same as the two above, but for a non binary tree
def iterative_dfs_graph(root):

    stack = []
    root.visited = True
    stack.append(root)

    val = ""

    while stack:

        node = stack.pop()
        val += node.val

        for neighbor in node.neighbors:

            if not neighbor.visited:
                neighbor.visited = True
                stack.append(neighbor)

    return val


def recursive_dfs_graph(node):
    if not node:
        return ""
    else:
        val = node.val
        for neighbor in node.neighbors:
            neighbor_val = recursive_dfs_graph(neighbor)
            val += neighbor_val
        return val


# Tests
from tests.trees import binary_tree, graph  # noqa

# Iterative DFS on a binary tree
expected = "abdecfg"
actual = iterative_dfs_binary_tree(binary_tree)
print("\nIterative DFS Binary Tree")
print("-" * 20)
print(expected == actual)

# Recursive DFS on a binary tree
expected = "abdecfg"
actual = recursive_dfs_binary_tree(binary_tree)
print("\nRecursive DFS Binary Tree")
print("-" * 20)
print(expected == actual)


# Iterative DFS on a non-binary graph
print("\nIterative DFS Graph")
print("-" * 20)
expected = "adcfhilkjgbe"
actual = iterative_dfs_graph(graph)
print(expected == actual)


# Recursive DFS on a non-binary graph
print(f"\nRecursive DFS on Graph")
print("-" * 20)
expected = "abecfghijkld"
actual = recursive_dfs_graph(graph)
print(expected == actual)
