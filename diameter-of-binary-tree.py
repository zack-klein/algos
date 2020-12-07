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
