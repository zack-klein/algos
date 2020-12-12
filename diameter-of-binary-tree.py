"""
https://leetcode.com/problems/diameter-of-binary-tree/
"""


# A little upset that I had to come and look at the solution for this one.
# Going to revisit it and try again.
def diameterOfBinaryTree(self, root):
    self.number_of_nodes = 1

    def dfs(node):

        if not node:
            return 0

        L = dfs(node.left)
        R = dfs(node.right)
        self.number_of_nodes = max(self.number_of_nodes, L + R + 1)
        return max(L, R) + 1

    dfs(root)

    return self.number_of_nodes - 1


# After redoing this 4 times I finally got it.
def diameterOfBinaryTreeRedo(self, root):
    self.max = 1

    def dfs(node):

        if node:
            L = dfs(node.left)
            R = dfs(node.right)
            self.max = max(self.max, L + R + 1)
            return max(L, R) + 1

        else:
            return 0

    dfs(root)

    return self.max - 1


# I'm a little upset that this one doesn't work. It passes the initial
# test case but fails when we see a root node with no children. I'm sure
# there's a way to get this one to work without having to do the magic
# number nonsense we have to do above.
def diameterOfBinaryTreeNoWork(self, root):
    self.max = 1

    def dfs(node):

        if node:
            L = dfs(node.left)
            R = dfs(node.right)
            self.max = max(self.max, L + R)
            return max(L, R) + 1

        else:
            return 0

    dfs(root)

    return self.max
