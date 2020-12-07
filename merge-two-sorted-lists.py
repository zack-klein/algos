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


# Done iteratively
def mergeTwoListsIterative(l1, l2):
    head = None
    prev = None
    L = l1
    R = l2

    while L or R:

        if L and R:

            if L.val <= R.val:
                current = L
                L = L.next

            elif R.val < L.val:
                current = R
                R = R.next

        elif L:
            current = L
            L = L.next

        elif R:
            current = R
            R = R.next

        if prev:
            prev.next = current
        else:
            head = current

        current.next = None
        prev = current

    return head


# Aaand recursively!
def mergeTwoListsRecursive(self, l1, l2):
    self.head = None
    self.prev = None

    def merge(L, R):
        if L or R:

            if L and R:

                if L.val <= R.val:
                    current = L
                    L = L.next

                elif R.val < L.val:
                    current = R
                    R = R.next

            elif L:
                current = L
                L = L.next

            elif R:
                current = R
                R = R.next

            if self.prev:
                self.prev.next = current
            else:
                self.head = current

            current.next = None
            self.prev = current

            merge(L, R)

    merge(l1, l2)

    return self.head
