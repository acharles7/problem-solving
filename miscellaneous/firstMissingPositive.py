"""
Given an unsorted integer array nums, 
find the smallest missing positive integer.

Follow up: Could you implement an algorithm that 
runs in O(n) time and uses constant extra space.?
"""

# time = O(n) space = O(n)
def firstMissingPositive(nums) -> int:
    if not nums: return 1
    visited = set(nums)

    for i in range(len(nums)+1):
        if i not in visited and i != 0:
            return i
    return i+1

# time = O(n) space = O(n)
def preprocess(nums):
    for i, num in enumerate(nums):
        if num <= 0 or num > len(nums):
            nums[i] = 1
    return nums
    
def firstMissingPositive(nums):
    if not nums: return 1

    if 1 not in nums:
        return 1

    nums = preprocess(nums)
    output = [0]*(len(nums)+1)

    for i in range(len(nums)):
        output[nums[i]] = 1

    for i in range(1, len(output)):
        if output[i] == 0:
            return i
    return i+1
  
    
# nums = [7,8,9,11,12]
# nums = [1,2,0]
# nums = [3,4,-1,1]
nums = [0]
first_missing_positive(nums)

