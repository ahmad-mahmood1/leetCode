def sort(stack, n):
    if not len(stack) or stack[-1] < n:
        stack.append(n)
        return 

    num = stack.pop()
    sort(stack, n)
    stack.append(num)


def sortStack(stack):
    if not len(stack):
        return stack

    num = stack.pop()

    sortStack(stack)

    sort(stack, num)



arr = [9, 8, -1, 2, 2, 3, 4, 10, 11]

sortStack(arr)
print(arr)
