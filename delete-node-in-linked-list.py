"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


# Feels like more of a trick question
def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
