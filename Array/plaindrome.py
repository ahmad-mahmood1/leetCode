def palindrome(arr):
    s = 0
    e = len(arr) - 1
    isPalindrome = True
    while s <= e:
        if arr[s] != arr[e]:
            isPalindrome = False
            break
        s += 1
        e -= 1
    return isPalindrome


arr = ["a", "f", "a", "b", "a"]

print(palindrome(arr))
