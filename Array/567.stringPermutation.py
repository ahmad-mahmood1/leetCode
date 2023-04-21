# s1 small perm string to check in string s2
def hasPermutation(s1, s2):
    arr1 = [0] * 26
    arr2 = [0] * 26
    print(arr1, arr2)

    def checkPerm(a1, a2):
        i = 0
        while i < 26:
            if a1[i] != a2[i]:
                return False
            i += 1
        return True

    for i in s1:
        arr1[ord(i) - 97] += 1

    i = 0
    windowSize = len(s1)

    while i < windowSize:
        arr2[ord(s2[i]) - 97] += 1
        i += 1
    if checkPerm(arr1, arr2):
        return True

    while i < len(s2):
        newChar = s2[i]
        oldChar = s2[i - windowSize]

        arr2[ord(newChar) - 97] += 1
        arr2[ord(oldChar) - 97] -= 1
        if checkPerm(arr1, arr2):
            return True
        i += 1

    return False


# Q. find permutation of a string
s1 = "ze"
s2 = "asdasdsdezasd"


print("answer", hasPermutation(s1, s2))
