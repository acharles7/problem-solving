# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.


def maxProduct(nums):
    if len(nums) < 1:
        return nums[0]

    current_l = nums[0]
    global_mul_l = nums[0]

    for i in range(1, len(nums)):
        if current_l == 0:
            current_l = nums[i]
        else:
            current_l = current_l * nums[i]

        global_mul_l = max(current_l, global_mul_l)
    current_r = nums[-1]
    global_mul_r = nums[-1]
    for i in list(reversed(nums))[1:]:
        if current_r == 0:
            current_r = i
        else:
            current_r = current_r * i
        global_mul_r = max(current_r, global_mul_r)
    return max(global_mul_r, global_mul_l)


A = [2, 3, -2, 4, 1, 2]
print(maxProduct(A))
