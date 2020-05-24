"""
https://leetcode.com/problems/linked-list-cycle-ii/
"""


def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None

    seen = {}

    while True:

        if head.next in seen:
            return seen[head.next]

        if not head.next:
            return None

        seen[head] = head

        head = head.next
