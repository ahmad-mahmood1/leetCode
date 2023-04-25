def fastExponentiation(x, n, m):
    res = 1
    while n > 0:
        if n % 2 != 0:
            res = (res * x % m) % m
        x = (x % m * x % m) % m
        n = n // 2

    return res


print(fastExponentiation(2, 11, 3))
