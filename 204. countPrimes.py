def countPrimes(n):
    primeArr = [True for i in range(n)]

    count = 0
    for i in range(2, n):
        if primeArr[i] == True:
            count += 1
            j = i * 2
            while j < n:
                primeArr[j] = False
                j = j + i
    return count


print(countPrimes(10))
