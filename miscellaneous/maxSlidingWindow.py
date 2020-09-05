'''
Optimized maximum sliding window (O(n))

Given an array nums, there is a sliding window of size k which is moving from the 
very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. Return the max sliding window.
'''

from collections import deque

def max_sliding_window(nums, k):

    def cleanups(i):
        if queue and queue[0] == i - k:
            queue.popleft()

        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

    queue = deque()
    max_idx = 0

    for i in range(k):
        cleanups(i)
        queue.append(i)

        if nums[i] > nums[max_idx]:
            max_idx = i
    out = [nums[max_idx]]
    
    for i in range(k, len(nums)):
        cleanups(i)
        queue.append(i)
        out.append(nums[queue[0]])
    return out

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_sliding_window(nums, k)

