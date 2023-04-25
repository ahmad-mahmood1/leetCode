import math


# GetPrime function gets all the primes in the range L to sqrt of R
def GetPrimes(prime, R):
    # A boolean array indicates the sieve
    c = [True] * (R + 1)

    M = int(math.sqrt(R))
    for i in range(2, M + 1):
        # removing the multiples if c[i] is true
        if c[i]:
            for j in range(i * i, M + 1, i):
                c[j] = False
    # traversing over the c array and getting all the primes in given range
    for l in range(2, M + 1):
        if c[l]:
            prime.append(l)


# A segment of  sieve used to get primes in given range[L, R]
# in segmented sieve we calculate primes in range [low,high]
# here we initially we find primes in range [2,sqrt(high)] to mark all their multiples as not prime
# then we mark all their(primes) multiples in range [low,high] as false
# this is a modified sieve of eratosthenes , in standard sieve of  eratosthenes we find prime from 1 to n(given number)
# in segmented sieve we only find primes in a given interval
def Segmented_Sieve(L, R):
    prime = list()
    GetPrimes(prime, R)
    # primes has primes in range [L,sqrt(R)]
    # dummy array to keep track of only between the given range
    # first element means L, second element means L+1 and so on.
    # dummy has elements between L and R so size is {R-L+1}
    dummy = [True] * (R - L + 1)
    # here dummy[0] indicates whether L is prime or not similarly dummy[1] indicates whether low+1 is prime or not
    for i in prime:
        # getting the first index for prime multiples in the given range
        low = L // i
        # here low means the first multiple of prime which is in range [L,R]
        if low <= 1:
            low = i + i
        elif (L % i) != 0:
            low = (low * i) + i
        else:
            low = low * i
        for j in range(low, R + 1, i):
            dummy[j - L] = False

    for k in range(L, R + 1):
        if dummy[k - L]:
            print(k, end=" ")


# DRIVER CODE
#   low must greater than or equal to 2
# L is the lower limit
# R is the upper limit
L = 110
R = 130
# Calling for segment of sieves to get the answer
print(Segmented_Sieve(L, R))
