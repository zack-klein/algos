"""
https://leetcode.com/problems/invert-binary-tree/
"""


def invertTree(root):
    if root:
        # Invert that sucka!
        left = root.left
        right = root.right

        root.left = right
        root.right = left

        invertTree(root.left)
        invertTree(root.right)

        return root
