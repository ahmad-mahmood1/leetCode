def sum(arr, i=0):
    if i == len(arr) - 1:
        return arr[i]

    return arr[i] + sum(arr, i + 1)

print(sum([1,2,3,4]))
