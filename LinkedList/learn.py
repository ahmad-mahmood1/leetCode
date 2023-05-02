class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.dataval)
            temp = temp.nextval

    def insertAtBeginning(self, newData):
        newNode = Node(newData)

        if linkedList.head is None and linkedList.tail is None:
            linkedList.head = newNode
            linkedList.tail = newNode
        else:
            newNode.nextval = self.head
            self.head = newNode

    def insertAtEnd(self, newData):
        newNode = Node(newData)
        if linkedList.head is None and linkedList.tail is None:
            linkedList.head = newNode
            linkedList.tail = newNode

        else:
            linkedList.tail.nextval = newNode
            linkedList.tail = newNode

    def insertAtPos(self, newData, pos):
        if pos == 0:
            self.insertAtBeginning(newData)
            return

        newNode = Node(newData)
        temp = self.head
        i = 0
        while temp is not None and i < pos - 1:
            if temp.nextval is None:
                self.insertAtEnd(newData)
                return
            temp = temp.nextval
            i += 1

        newNode.nextval = temp.nextval
        if temp.nextval is None:
            self.tail = newNode
        temp.nextval = newNode


def reverse(head: Node, tail: Node = None):
    prev = None
    current = head

    while current is not None:
        forward = current.nextval
        current.nextval = prev
        prev = current
        current = forward
    return prev


def recursiveReverse(current):
    if current is None or current.nextval is None:
        head = current
        return head

    newHead = recursiveReverse(current.nextval)

    current.nextval.nextval = current
    current.nextval = None

    return newHead


linkedList = LinkedList()

linkedList.insertAtEnd(12)
linkedList.insertAtEnd(13)
linkedList.insertAtEnd(14)
linkedList.insertAtEnd(15)

# linkedList.print()

# linkedList.head = reverse(linkedList.head)
linkedList.head = recursiveReverse(linkedList.head)

print("Reversed")
linkedList.print()
