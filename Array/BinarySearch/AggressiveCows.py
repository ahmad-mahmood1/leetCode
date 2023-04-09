def isPossible(arr, cows, minDistance):
    cowCount = 1
    lastPosition = arr[0]
    for i in range(len(arr)):
        if arr[i] - lastPosition >= minDistance:
            cowCount += 1
            if cowCount == cows:
                return True
            lastPosition = arr[i]

    return False


def aggressiveCows(arr, cows):
    arr = sorted(arr)
    answer = -1
    start, end = 0, max(arr)

    mid = (start + end) // 2

    while start <= end:
        if isPossible(arr, cows, mid):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
        mid = (start + end) // 2
    return answer


arr = [4, 2, 1, 3, 6]
cows = 3

print(
    "Minimum Distance between cows which is maximum of all possible distances",
    aggressiveCows(arr, cows),
)
