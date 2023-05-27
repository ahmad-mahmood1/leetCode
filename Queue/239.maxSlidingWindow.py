from collections import deque


def slidingWindowMaximum(nums, K):
    n = len(nums)
    if n * K == 0:
        return []
    if K == 1:
        return nums

    def clean_deque(i):
        #remove all elements indexes that are not within the current window size
        if deq and deq[0] == i - K:
            deq.popleft()
        #remove all elements which are smaller than the current element as this will be the new candidate for max number within the window
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()

    deq = deque()
    max_idx = 0
    for i in range(K):
        clean_deque(i)
        deq.append(i)
        if nums[i] > nums[max_idx]:
            max_idx = i
    output = [nums[max_idx]]

    for i in range(K, n):
        clean_deque(i)
        deq.append(i)
        
        #max element for the given window is at the front of the deque
        output.append(nums[deq[0]])
    return output


nums = [8, 1, 2, 0, 5]


print(slidingWindowMaximum(nums, 3))
