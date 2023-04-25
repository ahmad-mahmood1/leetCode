def searchInMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    rowIndex = 0
    colIndex = cols - 1

    while rowIndex < rows and colIndex >= 0:
        element = matrix[rowIndex][colIndex]
        if element == target:
            return True
        if element > target:
            colIndex -= 1
        else:
            rowIndex += 1
    return False


print(
    searchInMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        6,
    )
)
