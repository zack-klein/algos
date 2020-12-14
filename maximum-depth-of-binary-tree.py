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


# Exact same solution as above, but revisited a while later!
def maxDepth2(root):

    if not root:
        return 0
    else:
        L = maxDepth(root.left)
        R = maxDepth(root.right)
        return max(L, R) + 1
