# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums):
        current_sum = 0
        global_sum = -999999

        if(len(nums) == 1):
            return nums[0]

        for i in range(len(nums)):
            if(nums[i] + current_sum > nums[i]):
                current_sum = nums[i] + current_sum
            else:
                current_sum = nums[i]

            if(current_sum > global_sum):
                global_sum = current_sum
        return global_sum

A = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(A))
