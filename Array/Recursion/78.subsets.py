def subset(arr, index, ans, output):
    if index >= len(arr):
        ans.append(output)
        return
    # exclude case
    subset(arr, index + 1, ans, output)
    # include case
    subset(arr, index + 1, ans, output + [arr[index]])


ans = []
output = []

index = 0
arr = [1, 2, 3]
subset(arr, index, ans, output)
print(ans)
