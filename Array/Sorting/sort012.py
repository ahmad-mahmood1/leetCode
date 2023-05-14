def sort012(arr, n):
    # write your code here
    # don't return anything

    zeroCount = 0
    oneCount = 0
    twoCount = 0

    def recursiveSort(arr):
        nonlocal zeroCount, oneCount, twoCount

        if not len(arr):
            return

        num = arr.pop()

        if num == 0:
            zeroCount += 1
        if num == 1:
            oneCount += 1
        if num == 2:
            twoCount += 1

        recursiveSort(arr)

        if zeroCount:
            arr.append(0)
            zeroCount -= 1
        elif oneCount:
            arr.append(1)
            oneCount -= 1
        elif twoCount:
            arr.append(2)
            twoCount -= 1

    recursiveSort(arr)


arr = [0,1,2,2,1,0]


print(sort012(arr, len(arr)))
