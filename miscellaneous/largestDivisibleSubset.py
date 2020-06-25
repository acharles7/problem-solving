'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) 
of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
'''

def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    if len(nums) == 0: return []
    nums.sort()
    subset = [[num] for num in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(subset[i]) < len(subset[j]) + 1:
                subset[i] = subset[j] + [nums[i]]
    return max(subset, key=len)
