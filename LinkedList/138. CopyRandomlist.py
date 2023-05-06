class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def insertAtEnd(self, newData):
        newNode = Node(newData)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode


def withHashMap(head):
#utilize hash map for random pointer access
        hm, zero = dict(), Node(0)
        cur, copy = head, zero
        while cur:
            copy.next = Node(cur.val)
            hm[cur] = copy.next
            cur, copy = cur.next, copy.next
            
        cur, copy = head, zero.next
        while cur:
            copy.random = hm[cur.random] if cur.random else None
            cur, copy = cur.next, copy.next
                
        return zero.next


#with O(1) space complexity
def copyRandomList(head):
    originalHead = head
    cloneHead = None
    cloneTail = None

    # step 1 make a copy with random pointers

    temp = originalHead
    while temp is not None:
        data = temp.val
        node = Node(data)
        if cloneHead is None:
            cloneHead = node
            cloneTail = node
        else:
            cloneTail.next = node
            cloneTail = node
        temp = temp.next

    # step 2 point clone Node between two original Nodes
    originalTemp = head
    cloneTemp = cloneHead

    while originalTemp is not None and cloneTemp is not None:
        next = originalTemp.next

        originalTemp.next = cloneTemp
        originalTemp = next

        next = cloneTemp.next
        cloneTemp.next = originalTemp
        cloneTemp = next

    # step 3 copy random pointers
    originalTemp = head

    while originalTemp is not None:
        if originalTemp.next is not None:
            originalTemp.next.random = (
                originalTemp.random.next if originalTemp.random else originalTemp.random
            )
        originalTemp = originalTemp.next.next

    # step 4 revert both lists to original pointers
    originalTemp = head
    cloneTemp = cloneHead

    while originalTemp is not None and cloneTemp is not None:
        originalTemp.next = cloneTemp.next
        originalTemp = originalTemp.next

        cloneTemp.next = originalTemp.next if originalTemp else None
        cloneTemp = cloneTemp.next

    return cloneHead


original = LinkedList()

original.insertAtEnd(4)
original.insertAtEnd(5)
original.insertAtEnd(6)
original.insertAtEnd(7)
original.insertAtEnd(8)

original.print()


clone = copyRandomList(original.head)


temp = clone
while temp is not None:
    print(temp.val)
    temp = temp.next
