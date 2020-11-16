"""
https://leetcode.com/problems/range-sum-of-bst/submissions/
"""


# This just traverses the whole tree -- we don't do anything special knowing
# that it's a binary search tree.
class TraverseWholeTree:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def dfs(node):

            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                dfs(node.left)
                dfs(node.right)

        self.ans = 0
        dfs(root)

        return self.ans


# This one just traverses the parts of the tree that it has to.
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def dfs(node):

            if node:
                if low <= node.val <= high:
                    self.ans += node.val

                if node.val > low:
                    dfs(node.left)

                if node.val < high:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
