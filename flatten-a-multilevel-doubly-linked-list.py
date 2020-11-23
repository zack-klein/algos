"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/
"""


class Node:
    pass


class Solution:
    def flatten(head: "Node") -> "Node":

        if not head:
            return None

        nodes = []

        def process_node(node):
            if node:

                nodes.append(node.val)

                if node.child:
                    process_node(node.child)

                if node.next:
                    process_node(node.next)

        process_node(head)

        i = 0

        while i < len(nodes):
            new_node = Node(val=nodes[i])

            if i != 0:
                prev_node.next = new_node  # noqa
                new_node.prev = prev_node  # noqa
            else:
                new_head = new_node

            prev_node = new_node  # noqa
            i += 1

        return new_head
