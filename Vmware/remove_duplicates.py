from typing import List

"""
Given a sorted array nums, remove the duplicates in-place such 
that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates1(nums: List[int]) -> int:   
    ptr = 0
    n = 0
    while n < len(nums):
        curr = nums[n]
        while n < len(nums) and nums[n] == curr:
            n += 1
        nums[ptr] = curr
        ptr += 1
    return ptr 

"""
Given a sorted array nums, remove the duplicates in-place such 
that duplicates appeared at most twice and return the new length.
"""

def removeDuplicates2(nums: List[int]) -> int:
    ptr = 0
    n = 0
    while n < len(nums):
        curr = nums[n]
        double = 0
        while n < len(nums) and nums[n] == curr:
            n += 1
            double += 1
            if double <= 2:
                nums[ptr] = curr
                ptr += 1
    return ptr
        
print(removeDuplicates1([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
