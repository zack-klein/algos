"""
https://leetcode.com/problems/linked-list-cycle/submissions/

They wanted the memory address for this, not the value :(
"""

# Memory for this is linear. Can be reduced to constant.
def hasCycleLinear(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    seen = {}

    if not head:
        return False

    node = head
    pos = 0

    while True:

        if node in seen:
            return True

        seen[node] = pos

        if not node.next:
            return False
        else:
            node = node.next
            pos += 1


# Uses a two-pointer method
def hasCycleConstant(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:

        if not fast or not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

    return True
