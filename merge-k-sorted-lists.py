"""
https://leetcode.com/problems/merge-k-sorted-lists
"""


class ListNode(object):
    pass


# This fails on one of the edge cases, but the logic works
def mergeKLists(self, lists):
    all_values = []

    for l in lists:

        has_next = True
        current_list = l
        while has_next:

            all_values.append(current_list.val)

            if current_list.next:
                current_list = current_list.next
            else:
                has_next = False

    all_values.sort()

    all_nodes = []

    for i, val in enumerate(all_values):
        node = ListNode(val=val, next=None)
        all_nodes.append(node)

    for i, node in enumerate(all_nodes):

        if i != len(all_nodes) - 1:
            node.next = all_nodes[i + 1]

    return all_nodes[0]
