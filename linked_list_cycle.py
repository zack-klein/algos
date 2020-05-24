"""
https://leetcode.com/problems/linked-list-cycle/submissions/

They wanted the memory address for this, not the value :(
"""


def hasCycle(self, head):
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
