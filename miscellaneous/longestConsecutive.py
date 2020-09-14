'''
Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
'''

def longest_consecutive(nums):
    nums = sorted(list(set(nums)))
    if len(nums) == 1:
        return 1

    l, r = 0, 1
    prev = 0
    maximum = 0

    while r < len(nums):
        while r < len(nums) and nums[r] - nums[prev] == 1:
            r += 1
            prev += 1

        maximum = max(maximum, r-l)
        r += 1
        prev += 1
        l = prev
    return maximum

