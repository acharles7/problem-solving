# Given an integer array, find three numbers whose product is maximum and
# output the maximum product.
import sys

# Time Complexity: (N logN)
def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


# Time Complexity: N
def maximumProductN(nums):
    max1, max2, max3 = -10000, -10000, -10000
    min1, min2 = 10000, 10000

    for n in nums:
        if n <= min1:
            min2 = min1
            min1 = n
        elif n <= min2:
            min2 = n

        if n >= max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n >= max2:
            max3 = max2
            max2 = n
        elif n >= max3:
            max3 = n
    return max(max1 * max2 * max3, min1 * min2 * max1)


A = [1, 5, 6, 1, -4, -2, -1, 2, 3, 10]
print(maximumProductN(A))
