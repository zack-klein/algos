"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


class TreeNode:
    pass


def maxDepth(root: TreeNode) -> int:

    if root:
        l = maxDepth(root.left)  # noqa
        r = maxDepth(root.right)
        return max(l, r) + 1
    else:
        return 0
