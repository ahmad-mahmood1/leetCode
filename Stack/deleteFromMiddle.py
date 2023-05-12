def delMid(arr, i):
    size = len(arr)

    mid = size // 2

    if size % 2:
        mid -= 1
    if i == mid:
        arr.pop()
        return

    num = arr.pop()

    delMid(arr, i - 1)

    arr.append(num)


arr = [1, 2, 3, 4, 5]

delMid(arr, len(arr) - 1)

print(arr)

