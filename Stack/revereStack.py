def appendToBottom(stack, num):
    if len(stack) == 0:
        stack.append(num)
        return stack

    x = stack.pop()

    appendToBottom(stack, num)

    stack.append(x)

    return stack


def reverseStack(arr):
    if len(arr) == 0:
        return arr

    num = arr.pop()

    reversedStack = reverseStack(arr)

    return appendToBottom(reversedStack, num)


s = [2,3,4,5,9,1,8]

print(reverseStack(s))
