# return an array output such that output[i] is equal to the product of all
# the elements of nums except nums[i].

def productExceptSelf(nums):
    res = []
    def calculateMul(A):
        mul = 1
        for i in A:
            mul *= i
        return mul

    for i in range(len(nums)):
        fh = nums[:i]
        sh = nums[i+1:]
        res.append(calculateMul(fh+sh))
    return res

A = [1,2,3,4]
print(productExceptSelf(A))
