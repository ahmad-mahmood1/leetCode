# Your task is to complete all these function's
# function should append an element on to the stack
min = 0


def push(arr, ele):
    # Code here
    global min
    if len(arr) == 0:
        arr.append(ele)
        min = ele
    else:
        if ele < arr[-1]:
            arr.append(2 * ele - min)
            min = ele
        else:
            arr.append(ele)


# Function should pop an element from stack
def pop(arr):
    # Code here
    global min
    if not len(arr):
        return

    else:
        current = arr.pop()
        if current > min:
            return current
        else:
            prev = min
            val = 2*min - current
            min = val
            return prev


# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return len(arr) == n


# function should return 1/0 or True/False
def isEmpty(arr):
    # Code here
    return len(arr) == 0


# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    global min
    return min


arr = []

push(arr, 5)
push(arr, 3)
push(arr, 4)
push(arr, 2)
pop(arr)
print(arr, getMin(len(arr), arr))
