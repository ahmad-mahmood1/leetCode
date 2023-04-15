# bubble sort -> On each loop, compare element next to current index, if smaller than current index, swap them. On every loop end, the maximum value item would be at the end of
# the array


def bubbleSort(arr):
    swaps = False
    print(swaps, "HERE SWPS", range(len(arr) - 1, 0))

    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True
        if swaps == False:
            break
    return arr


arr = [1, 14, 15, 2, 5, 3, 9]

print("bubble sort", bubbleSort(arr))
