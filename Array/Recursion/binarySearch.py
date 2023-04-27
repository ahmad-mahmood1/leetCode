def binarySearch(arr, start, end, target):
    if start > end:
        return False

    mid = (start + end) // 2
    if arr[mid] == target:
        return True

    if arr[mid] < target:
        return binarySearch(arr, start + 1, end, target)

    else:
        return binarySearch(arr, start, end - 1, target)


print(binarySearch([2, 3, 5, 6, 7], 0, 4, 8))
