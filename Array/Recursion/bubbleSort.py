def bubbleSort(arr, n):
    print(arr, n)
    if n == 0:
        return arr

    swaps = False
    for i in range(0, n):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swaps = True
    if not swaps:
        return arr

    return bubbleSort(arr, n - 1)


print(bubbleSort([1, 4, 5, 7, 6], 4))
