def minCost(stack):
    s = []

    for b in stack:
        if b == "{":
            s.append(b)
        else:
            if len(s) and s[-1] == "{":
                s.pop()
            else:
                s.push(b)

    a, b = 0, 0

    for bracket in s:
        if bracket == "{":
            a += 1
        else:
            b += 1

    cost = ((a + 1) // 2) + ((b + 1) // 2)

    return cost


str = "{{{{"

print(minCost(str))
