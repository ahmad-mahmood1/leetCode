# merge sort modified to count the no of inversions done where a inversion occurs when a[j] > a[i] and i > j


def merge(arr1, arr2, inversion_count=0):
    list_sorted = []
    while arr1 != [] and arr2 != []:
        if arr1[0] < arr2[0]:
            list_sorted.append(arr1.pop(0))
        else:
            list_sorted.append(arr2.pop(0))
            inversion_count += len(arr1)

    if len(arr1) < 1:
        list_sorted += arr2
    else:
        list_sorted += arr1

    return list_sorted, inversion_count


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    front, inversion_count_f = mergeSort(arr[:mid])
    back, inversion_count_b = mergeSort(arr[mid:])

    return merge(front, back, inversion_count_b + inversion_count_f)


print(mergeSort([8, 4, 2, 1]))
