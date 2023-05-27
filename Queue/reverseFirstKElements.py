# https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1

# Function to reverse first k elements of a queue.
from collections import deque


def modifyQueue(q, k):
    que = deque(q)
    stack = []

    for _ in range(k):
        ele = que.popleft()
        stack.append(ele)

    for i in range(len(stack) - 1, -1, -1):
        que.append(stack[i])

    for _ in range(0, len(q) - k):
        item = que.popleft()
        que.append(item)

    return list(que)


num = [1, 2, 3, 4, 5]
k = 3

print(modifyQueue(num, k))
