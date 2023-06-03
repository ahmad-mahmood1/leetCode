# https://leetcode.com/problems/balanced-binary-tree/description/

from queue import Queue
from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


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


def isBalanced(root):
    if not root:
        return True, 0

    leftBalanced, leftHeight = isBalanced(root.left)
    rightBalanced, rightHeight = isBalanced(root.right)

    diff = abs(leftHeight - rightHeight)

    checkBalance = diff <= 1
    ans = (
        leftBalanced and rightBalanced and checkBalance,
        max(leftHeight, rightHeight) + 1,
    )
    print(ans,"for node", root.data, "whose left and right is", root.left.data if root.left else None, root.right.data if root.right else None)
    return ans


levelOrderInput = deque([1, 2, 2, 3, 3, - 1, -1, 4, 4,-1,-1,-1,-1,-1,-1,-1,-1])
rootNode = buildFromLevelOrder()


isBalanced(rootNode)
