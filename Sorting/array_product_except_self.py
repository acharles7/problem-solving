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


def productExceptSelf2(A):
    res = []
    cur = 1
    for i in range(len(A)):
        res.append(cur)
        cur = cur * A[i]
    print(A)
    print(res)
    rev = 1
    for i in range(len(A) - 1, -1 , -1):
        res[i] = res[i] * rev
        rev = rev * A[i]
    return res

A = [1,2,3,2,1,5]
print(productExceptSelf2(A))
