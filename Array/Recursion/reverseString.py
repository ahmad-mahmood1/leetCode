def reverseString(str):
    if len(str) == 0:
        return str

    return reverseString(str[1:]) + str[0]


str = "abcde"
print(reverseString(str))
