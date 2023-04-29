def subsequence(str, i, ans, output):
    if i >= len(str):
        if output:
            ans.append(output)
        return

    char = str[i]

    subsequence(str, i + 1, ans, output + char)
    subsequence(str, i + 1, ans, output)


str = "abc"
i = 0
ans = []
output = ""

subsequence(str, i, ans, output)

print(ans)
