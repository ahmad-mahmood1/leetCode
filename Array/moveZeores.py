# move all zeroes to right in an  array


def moveArray(arr):
    if len(arr) == 1:
        return arr
    i = arr.index(0)
    for j in range(i + 1, len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]

            i += 1
    return arr


arr = [2,0,1,1,0,0,2]


print(moveArray(arr))
