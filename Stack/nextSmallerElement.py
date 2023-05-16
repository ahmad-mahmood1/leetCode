def nextSmallerElement(arr):
    stack = [-1]
    for i in range(len(arr) - 1, -1, -1):
        while stack[-1] >= arr[i]:
            stack.pop()

        stack.append(arr[i])

        arr[i] = stack[-2]

    return arr


arr = [3,3,1,1]

print(nextSmallerElement(arr))
