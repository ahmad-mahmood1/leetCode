def celebrity(matrix, n):
    adj = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj[i].append(j)

    for i in range(n):
        if not adj[i]:
            flag = True

            for j in range(n):
                if i == j:
                    continue
                if i not in adj[j]:
                    flag = False
                    break
            if flag:
                return i
    return -1


M = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]

print(celebrity(M, len(M)))
