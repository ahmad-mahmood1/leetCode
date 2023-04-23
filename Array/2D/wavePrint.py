#print 2d array column wise, fisrt read is top to bottom and next is bottom to top, continues in the same pattern

def wavePrint(arr, rows, cols):
    ans = []
    for col in range(cols):
        if col % 2 == 0:
            row = 0
            while row < rows:
                ans.append(arr[row][col])
                row += 1
        else:
            row = rows - 1
            while row >= 0:
                ans.append(arr[row][col])
                row -= 1
    return ans


print(wavePrint([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3))
