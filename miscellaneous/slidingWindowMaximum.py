from collections import deque

''' 
Given an array nums, there is a sliding window of size k which is moving from 
the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. Return the max sliding window.
'''


def maxSlidingWinidow(nums, k):
    if not nums:
        return []

    def removeElements(i):
        if queue and queue[0] == i-k:
            queue.popleft()                
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

    max_id = 0
    queue = deque()
    for i in range(k):
        removeElements(i)
        queue.append(i)
        if nums[i] > nums[max_id]:
            max_id = i
    output = [nums[max_id]]

    for i in range(k, len(nums)):
        removeElements(i)
        queue.append(i)
        output.append(nums[queue[0]])
    return output
