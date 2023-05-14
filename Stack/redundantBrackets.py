def hasRedundants(stack, arg=None):
    if not len(stack):
        return False

    if arg == stack[-1]:
        return True

    exp = stack.pop()

    ans =  hasRedundants(stack, exp)
    return ans

str = "(a+b)"


print(hasRedundants(list(str)))
