"""
https://leetcode.com/problems/reorder-list/submissions/
"""


def reorderListBruteForce(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if not head:
        return head

    pos = 0
    hash_table = {}
    building_ht = True
    node = head

    while building_ht:

        if not node.next:
            building_ht = False

        hash_table[pos] = node

        node = node.next
        pos += 1

    i = 0
    counter = 0

    current = head

    while counter < len(hash_table) - 1:
        left_new_pointer = hash_table[(len(hash_table) - 1) - i]
        current.next = left_new_pointer
        left_new_pointer.next = None
        counter += 1

        current = left_new_pointer
        right_new_pointer = hash_table[i + 1]
        current.next = right_new_pointer
        right_new_pointer.next = None
        counter += 1

        i += 1
        current = hash_table[i]
