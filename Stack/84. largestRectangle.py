def prevSmallerValIndexes(arr):
    stack = [-1]
    ans = [0] * len(arr)
    for i in range(len(arr)):
        while stack[-1] != -1 and arr[stack[-1]] >= arr[i]:
            stack.pop()

        ans[i] = stack[-1]
        stack.append(i)
    return ans


def nextSmallerValIndexes(arr):
    stack = [-1]
    ans = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack[-1] != -1 and arr[stack[-1]] >= arr[i]:
            stack.pop()

        ans[i] = stack[-1]
        stack.append(i)
    return ans


def largestRectangle(heights):
    prev = prevSmallerValIndexes(heights)
    next = nextSmallerValIndexes(heights)
    area = -1
    for i in range(len(heights)):
        l = heights[i]

        if next[i] == -1:
            next[i] = len(heights)

        w = next[i] - prev[i] - 1
        newArea = l * w
        area = max(area, newArea)

    return area


heights = [2, 1, 5, 6, 2, 3]

print(largestRectangle(heights))
