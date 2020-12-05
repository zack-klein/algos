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
