def merge(arr1, arr2):
    list_sorted = []
    while arr1 != [] and arr2 != []:
        if arr1[0] < arr2[0]:
            list_sorted.append(arr1.pop(0))
        else:
            list_sorted.append(arr2.pop(0))
    if len(arr1) < 1:
        list_sorted += arr2
    else:
        list_sorted += arr1

    return list_sorted


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    front = mergeSort(arr[:mid])
    back = mergeSort(arr[mid:])

    return merge(front, back)


print(mergeSort([4, 3, 2, 9, 8, 7]))
