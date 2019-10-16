def findSubarray(nums, k):
    out = []
    for i in range(len(nums)):
        currMin = float('inf')
        currMax = -float('inf')
        for j in range(i+1, len(nums)+1):
            currMin = min(currMin, nums[j-1])
            currMax = max(currMax, nums[j-1])
            if currMax - currMin == (j-i) - 1:
                out.append(nums[i:j])
    return out

nums = [0, 4, 3, 1, 2, 5]
k = 10
print(findSubarray(nums, k))
