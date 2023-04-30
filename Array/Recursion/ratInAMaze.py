maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
rows, cols = len(maze), len(maze)

visited = [[0 for _ in range(len(maze))] for _ in range(len(maze))]
visited[0][0] = 1


def validMove(matrix, i, j, visited):
    return (
        i >= 0
        and j >= 0
        and i < rows
        and j < cols
        and matrix[i][j] == 1
        and visited[i][j] == 0
    )


def getToDestination(matrix, i, j, path, visited, ans):
    if i == rows - 1 and j == cols - 1:
        ans.append(path)
        return

    # up
    if validMove(matrix, i - 1, j, visited):
        visited[i - 1][j] = 1
        getToDestination(matrix, i - 1, j, path + "U", visited, ans)
        visited[i - 1][j] = 0

    # down
    if validMove(matrix, i + 1, j, visited):
        visited[i + 1][j] = 1
        getToDestination(matrix, i + 1, j, path + "D", visited, ans)
        visited[i + 1][j] = 0

    # right
    if validMove(matrix, i, j + 1, visited):
        visited[i][j + 1] = 1
        getToDestination(matrix, i, j + 1, path + "R", visited, ans)
        visited[i][j + 1] = 0

    # left
    if validMove(matrix, i, j - 1, visited):
        visited[i][j - 1] = 1
        getToDestination(matrix, i, j - 1, path + "L", visited, ans)
        visited[i][j - 1] = 0


ans = []
getToDestination(maze, 0, 0, "", visited, ans)
print(ans)
