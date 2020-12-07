"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Gross, slow, and fat - but works!
def mergeTwoLists(l1, l2):

    nodes = []
    left = l1
    right = l2

    while left or right:

        if left and not right:
            nodes.append(left)
            left = left.next

        elif right and not left:
            nodes.append(right)
            right = right.next

        elif left.val <= right.val:
            nodes.append(left)
            left = left.next

        elif right.val <= left.val:
            nodes.append(right)
            right = right.next

    head = None

    for i, node in enumerate(nodes):

        if i == 0:
            head = node

        if i != len(nodes) - 1:
            next_node = nodes[i + 1]
            next_node.next = None
        else:
            next_node = None

        node.next = next_node

    return head
