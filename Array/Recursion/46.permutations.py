nums = [1, 2, 3]
ans = []


def permutation(res, i=0):
    if i >= len(nums):
        ans.append(res[:])
        return
    for k in range(i, len(nums)):
        res[k], res[i] = res[i], res[k]
        permutation(res, i + 1)
        res[i], res[k] = res[k], res[i]


permutation(nums)

print(ans)
