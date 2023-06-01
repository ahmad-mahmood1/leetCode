from queue import Queue
from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def buildTree(node=None):
    global inputArr
    data = inputArr.popleft()

    if int(data) == -1:
        return None

    node = Node(data)

    print("Enter left of", data)

    node.left = buildTree(node.left)

    print("Enter right of", data)

    node.right = buildTree(node.right)

    return node


def levelOrderTraversal(root):
    q = Queue(-1)

    q.put(root)
    q.put(None)
    while not q.empty():
        node = q.get()
        if not node:
            print("\n")
            if not q.empty():
                q.put(None)
        else:
            print(node.data, end=" ")
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)


def reverseLevelOrder(root):
    if not root or not root.data:
        return None
    ans = deque()
    q = Queue(-1)
    q.put(root)
    q.put(None)

    while not q.empty():
        node = q.get()
        if not node:
            if not q.empty():
                q.put(None)
                ans.appendleft(None)
        else:
            ans.appendleft(node.data)
            if node.right:
                q.put(node.right)

            if node.left:
                q.put(node.left)

    for i in ans:
        if not i:
            print("\n")
        else:
            print(i, end=" ")


def inOrderTraversal(node):
    if not node:
        return None

    inOrderTraversal(node.left)

    print(node.data, end=" ")

    inOrderTraversal(node.right)


def preOrderTraversal(node):
    if not node:
        return None

    print(node.data, end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def postOrderTraversal(node):
    if not node:
        return None

    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=" ")


def buildFromLevelOrder():
    global levelOrderInput
    q = Queue(-1)
    data = levelOrderInput.popleft()
    root = Node(data)

    q.put(root)

    while not q.empty():
        node = q.get()

        data = levelOrderInput.popleft()
        if data != -1:
            node.left = Node(data)
            q.put(node.left)

        data = levelOrderInput.popleft()
        if data != -1:
            node.right = Node(data)
            q.put(node.right)
    return root


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


inputArr = deque([1, 3, 7, -1, -1, 11, -1, -1, 5, 17, -1, -1, -1])

levelOrderInput = deque([1, 3, 5, 7, 11, 17, -1, -1, -1, -1, -1, -1, -1])

# rootNode = buildTree()
rootNode = buildFromLevelOrder()

levelOrderTraversal(rootNode)

# reverseLevelOrder(rootNode)


# print()
# print(height(rootNode))


# preOrderTraversal(rootNode)
# print()
# inOrderTraversal(rootNode)
# print()
# postOrderTraversal(rootNode)
