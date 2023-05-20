def largestRectangle(matrix):
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

    rows = len(matrix)
    cols = len(matrix[0])

    baseRow = [0] * cols

    area = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != "0":
                baseRow[j] = baseRow[j] + int(matrix[i][j])
            else:
                baseRow[j] = 0

        newArea = largestRectangle(baseRow)

        area = max(area, newArea)

    return area


# matrix = [
#     ["1", "0", "1", "0", "0"],
#     ["1", "0", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "0", "0", "1", "0"],
# ]

matrix = [["0", "1"], ["1", "0"]]

print(largestRectangle(matrix))
