class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, newData):
        newNode = Node(newData)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


def sortList(head):
    zeroCount, oneCount, twoCount = 0, 0, 0

    temp = head
    while temp is not None:
        if temp.data == 0:
            zeroCount += 1
        if temp.data == 1:
            oneCount += 1
        if temp.data == 2:
            twoCount += 1

        temp = temp.next

    while head is not None:
        if zeroCount != 0:
            head.data = 0
            zeroCount -= 1

        elif oneCount != 0:
            head.data = 1
            oneCount -= 1
        elif twoCount != 0:
            head.data = 2
            twoCount -= 1
        
        head = head.next


linkedList = LinkedList()

linkedList.insertAtEnd(1)
linkedList.insertAtEnd(1)
linkedList.insertAtEnd(0)
linkedList.insertAtEnd(2)
linkedList.insertAtEnd(0)
linkedList.insertAtEnd(2)


sortList(linkedList.head)
linkedList.print()
