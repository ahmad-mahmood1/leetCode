def reverseWords(arr):
    def revWord(arr, s, e):
        while s < e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

    ws, we = 0, 0

    # reverse words in a string
    for i in range(len(arr)):
        if arr[i] == " ":
            we = i - 1
            revWord(arr, ws, we)
            ws = i + 1
        elif i + 1 == len(arr):
            revWord(arr, ws, i)

    # reverse the whole string
    s, e = 0, len(arr) - 1

    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
    return arr


arr = ["a", "h", "m", "a", "d", " ", "i", "s", " ", "h", "e", "r", "e"]

print(reverseWords(arr))
