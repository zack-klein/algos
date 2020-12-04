class TreeNode(object):
    def __init__(self, *args, **kwargs):
        pass


def mergeTrees(t1, t2):
    if t1 and t2:
        root = TreeNode(val=t1.val + t2.val)
        root.left = mergeTrees(t1.left, t2.left)
        root.right = mergeTrees(t1.right, t2.right)
        return root

    else:
        return t1 or t2
