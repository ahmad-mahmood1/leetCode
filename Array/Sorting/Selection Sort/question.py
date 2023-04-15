# selection sort -> on each loop find smallest value on the subsequent indexes, if found smallest, swap the element to current index. 


def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        
    return arr


arr = [2, 4, 15, 12, 10, 0]

print("sorted arr",selectionSort(arr))