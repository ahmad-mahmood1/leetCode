def nextSmallerElement(arr):
    stack = [-1]
    for i in range(len(arr) - 1, -1, -1):
        while stack[-1] != -1 and stack[-1] >= arr[i]:
            stack.pop()
        
        item = arr[i]    
        arr[i] = stack[-1]
        stack.append(item)

    return arr


arr = [3, 8, 5, 2, 25]

print(nextSmallerElement(arr))
