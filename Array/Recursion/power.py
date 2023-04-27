def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base

    ans = power(base, exp // 2)

    if exp % 2 == 0:
        return ans * ans

    return base * ans * ans


print(power(2, 4))
