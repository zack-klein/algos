"""
Some practice on recursion.
"""

# There are two ways to maintain the state of a recursive function:
#   - Threading the state through each recursive call (and the call stack)
#   - Mutating global state
#
# In Python, this translates to:
#   1. Passing the "updated" state to each call of the recursive function
#   2. Using a global variable (or a self.<var> of a class) to track state
#
# Great article that helps to explain this:
# https://realpython.com/python-thinking-recursively/#maintaining-state


# Here's an example of using threading to get a string of all the values of a
# binary tree. This was weirdly hard for me to wrap my head around for some
# reason...
def recursive_threading(node):
    if not node:
        return ""
    else:
        L = recursive_threading(node.left)
        R = recursive_threading(node.right)
        return node.val + L + R


# And here's the same example using global state. This was easier for me to
# get at first but I can see why people are not wild about using global state.
string_of_all_nodes = ""


def recursive_global(node):
    if node:
        global string_of_all_nodes
        string_of_all_nodes += node.val
        recursive_global(node.left)
        recursive_global(node.right)


from tests.trees import binary_tree  # noqa

print("\nThreading Recursion")
print("-" * 20)
expected = "abdecfg"
actual = recursive_threading(binary_tree)
print(expected == actual)


print("\nGlobal State Recursion")
print("-" * 20)
expected = "abdecfg"
recursive_global(binary_tree)
actual = string_of_all_nodes
print(expected == actual)
