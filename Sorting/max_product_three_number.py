# Given an integer array, find three numbers whose product is maximum and
# output the maximum product.

def maximumProduct(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

A = [1,5,6,1,-2,-2,-1,2,3]
print(maximumProduct(A))
