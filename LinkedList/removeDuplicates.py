class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self, msg):
        print(msg)
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insertAtBeginning(self, newData):
        newNode = Node(newData)

        if linkedList.head is None and linkedList.tail is None:
            linkedList.head = newNode
            linkedList.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, newData):
        newNode = Node(newData)
        if linkedList.head is None and linkedList.tail is None:
            linkedList.head = newNode
            linkedList.tail = newNode

        else:
            linkedList.tail.next = newNode
            linkedList.tail = newNode

    def insertAtPos(self, newData, pos):
        if pos == 0:
            self.insertAtBeginning(newData)
            return

        newNode = Node(newData)
        temp = self.head
        i = 0
        while temp is not None and i < pos - 1:
            if temp.next is None:
                self.insertAtEnd(newData)
                return
            temp = temp.next
            i += 1

        newNode.next = temp.next
        if temp.next is None:
            self.tail = newNode
        temp.next = newNode

    def sortedMerge(self, a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):
        if h == None or h.next == None:
            return h

        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.mergeSort(h)

        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)

        # Merge the left and right lists
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    # Utility function to get the middle
    # of the linked list
    def getMiddle(self, head):
        if head == None:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def removeDuplicates(self):
        current = self.head
        index = None

        # Loop to traverse the linked list
        while current is not None:
            # Loop to compare current node with all other nodes
            index = current.next
            while index is not None:
                # Checking for duplicate values
                if current.data == index.data:
                    # Deleting the duplicate node
                    current.next = index.next
                    index = current.next
                else:
                    index = index.next
            current = current.next


linkedList = LinkedList()

linkedList.insertAtEnd(12)
linkedList.insertAtEnd(13)
linkedList.insertAtEnd(19)
linkedList.insertAtEnd(13)
linkedList.insertAtEnd(13)
linkedList.insertAtEnd(13)
linkedList.insertAtEnd(21)
linkedList.insertAtEnd(15)
linkedList.insertAtEnd(16)
linkedList.insertAtEnd(16)
linkedList.insertAtEnd(16)
linkedList.insertAtEnd(17)

linkedList.print("List")


linkedList.mergeSort(linkedList.head)

linkedList.removeDuplicates()

linkedList.print("After sorting and removal")
