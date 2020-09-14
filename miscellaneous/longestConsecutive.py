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


# Using heap

import heapq

def longest_consecutive(nums):
    if not nums: return 0
        
    heapq.heapify(nums)
    maximum, count = 0, 1
    prev = heapq.heappop(nums)

    while nums:
        curr = heapq.heappop(nums)
        if curr - prev == 1:
            count += 1
        elif curr - prev == 0:
            count += 0
        else:
            maximum = max(maximum, count)
            count = 1
        prev = curr
    return max(maximum, count)


