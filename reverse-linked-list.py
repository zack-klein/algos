# Iterative
def reverseList(head):

    previous = None
    current = head

    while current:
        temp_next = current.next
        current.next = previous
        previous = current
        current = temp_next

    return previous


# Recursively
def reverseListRecursive(head):

    new_head = head  # noqa

    def reverse(node):
        if node and node.next:
            reverse(node.next)
            node.next.next = node
            node.next = None
        else:
            new_head = node  # noqa

    reverse(head)

    return new_head
