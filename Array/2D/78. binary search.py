def findInMatrix(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])

    start = 0
    end = (rows * columns) - 1

    mid = (start + end) // 2

    while start <= end:
        element = matrix[mid // columns][mid % columns]
        print("element", element, "at index", mid)
        if element == target:
            return True

        if element < target:
            start = mid + 1

        if element > target:
            end = mid - 1

        mid = (start + end) // 2

    return False


print(findInMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
