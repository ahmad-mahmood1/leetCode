def partition(arr, s, e):
    pivotIndex = s

    # count elements smaller than arr[pivotIndex] and replace arr[pivotIndex] with arr[pivotIndex+no of elements]
    count = 0
    for i in range(s + 1, e + 1):
        if arr[i] <= arr[pivotIndex]:
            count += 1

    arr[pivotIndex], arr[pivotIndex + count] = arr[pivotIndex + count], arr[pivotIndex]

    pivotIndex += count
    i, j = s, e

    while i < pivotIndex and j > pivotIndex:
        while arr[i] < arr[pivotIndex]:
            i += 1
        while arr[j] > arr[pivotIndex]:
            j -= 1

        if i < pivotIndex and j > pivotIndex:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    print("paritioned for index ", s, e, arr, "pivotIndex is", pivotIndex)
    return pivotIndex


def quickSort(arr, s, e):
    if s >= e:
        return arr

    pivotIndex = partition(arr, s, e)

    quickSort(arr, s, pivotIndex - 1)

    quickSort(arr, pivotIndex + 1, e)

    print("returning", arr, s, e)


arr = [4, 3, 2, 1, 4, 4, 5, 10, 6, 1]
print(quickSort(arr, 0, len(arr) - 1))
print("ans", arr)
