# Given an array of number nums and an int k. Return the product of every k consecutive numbers.

#Time Complexity: N x k
def consecutiveProduct(nums, k):
    def multi(A):
        mul = 1
        for i in A:
            mul *= i
        return mul
    output = []
    for i in range(k - 1):
        nums.insert(0,1)

    for i in range(0,len(nums) -  k + 1):
        output.append(multi(nums[i:i+k]))
    return output

#Time Complexity: N
def consecutiveProduct1(nums, k):
    product = 1
    output = []
    for i in range(len(nums)):
        product *= nums[i]
        if i < k:
            product //= 1
        else:
            product //= nums[i - k]
        output.append(product)
    return output

nums = [1, 3, 3, 6, 5, 7, 0, -3]
k = 3
print(consecutiveProduct1(nums, k))

# Output: [1, 3, 9, 54, 90, 210, 0, 0]
# Explanation: 1 (1), 3 (1x3), 9 (1x3x3), 54 (3x3x6), 90 (3x6x5), 210 (6x5x7), 0 (5x7x0), 0 (7x0x3)
