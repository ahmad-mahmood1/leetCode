def isPossible(arr, requiredWood, bladeHeight):
    woodCut = 0
    for i in range(len(arr)):
        wood_acquired = 0
        if arr[i] > bladeHeight:
            wood_acquired = arr[i] - bladeHeight
        woodCut += wood_acquired

    if woodCut >= requiredWood:
        return True

    return False


def chopMinimumWood(arr, minWood):
    arr = sorted(arr)
    answer = -1
    start, end = 0, max(arr)

    mid = (start + end) // 2

    while start <= end:
        if isPossible(arr, minWood, mid):
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
        mid = (start + end) // 2
    return answer


arr = [4, 42, 40, 26, 46]
minWood = 20

print(
    "Minimum Distance between minWood which is maximum of all possible distances",
    chopMinimumWood(arr, minWood),
)
