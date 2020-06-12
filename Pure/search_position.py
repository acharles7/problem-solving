'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''


def searchInsert(nums, target) -> int:   
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l =  mid + 1
        else:
            r =  mid - 1
    return l
