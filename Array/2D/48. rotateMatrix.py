##rotate matrix by 90 degree


def rotateMatrix(matrix):
    rows = len(matrix)

    # transpose of matrix
    ## only traverse lower right triangle
    row = 1
    while row <= rows - 1:
        col = 0
        while col < row:
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            col += 1
        row += 1
    # reverse each row
    for i in range(rows):
        matrix[i] = matrix[i][::-1]
    return matrix


print(rotateMatrix([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
