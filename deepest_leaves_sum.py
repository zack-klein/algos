"""
https://leetcode.com/problems/deepest-leaves-sum/
"""


# Using a while loop to do a level order search
def deepestLeavesSumWhileLoop(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    current_level = [root] if root else []

    while True:
        next_level = []

        for element in current_level:

            if element.left is not None:
                next_level.append(element.left)

            if element.right is not None:
                next_level.append(element.right)

        if not next_level:
            return sum(e.val for e in current_level)
        current_level = next_level
