def spiralMatrix(matrix, rows, cols):
    count = 0
    startingRow = 0
    startingCol = 0
    endingRow = rows - 1
    endingCol = cols - 1
    ans = []

    while count < rows * cols:
        # printing top row
        if count < rows * cols:
            for i in range(startingCol, endingCol + 1):
                ans.append(matrix[startingRow][i])
                count += 1
            startingRow += 1

        # printing right col
        if count < rows * cols:
            for i in range(startingRow, endingRow + 1):
                ans.append(matrix[i][endingCol])
                count += 1
            endingCol -= 1

        # printing bottom row
        if count < rows * cols:
            for i in range(endingCol, startingCol - 1, -1):
                ans.append(matrix[endingRow][i])
                count += 1
            endingRow -= 1

        # printing left col
        if count < rows * cols:
            for i in range(endingRow, startingRow - 1, -1):
                ans.append(matrix[i][startingCol])
                count += 1
            startingCol += 1

    return ans


print(spiralMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3))
