def sortedMerge(a, b):
    result = None

    if a == None:
        return b
    if b == None:
        return a

    if a.data <= b.data:
        result = a
        result.child = sortedMerge(a.child, b)
    else:
        result = b
        result.child = sortedMerge(a, b.child)
    return result


def flattenLinkedList(head):
    if head is None or head.next is None:
        return head

    flatListHead = flattenLinkedList(head.next)
    head.next = None

    newHead = sortedMerge(head, flatListHead)

    return newHead
