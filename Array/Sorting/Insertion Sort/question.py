# insertion sort -> Compare current index value to previous indexes values, keep on moving the current index to left till it is in its right spot.


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j >= 1:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


arr = [14, 1, 3, 1, 12, 10, 7, 8, 9, 0]

print("insertion sort", insertionSort(arr))
