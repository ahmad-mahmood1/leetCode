digits = "23"
dic = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
ans = []


def letterComb(combination):
    #base case - when string combination len is equal to digits len append the string combination
    if len(combination) == len(digits):
        ans.append(combination)
    else:
        for str in dic[digits[len(combination)]]:
            letterComb(combination + str)


letterComb("")

print(ans)
