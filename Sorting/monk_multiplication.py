# find the product of the largest, second largest and the third largest
# integer in the range [1,i]


def multiplyRange(M):
    mul = 1
    for ele in M:
        mul = mul * ele
    return mul


def find_numbers(A, start, end):
    range_sorted = sorted(A[start : end + 1])
    size = len(range_sorted)
    if size == 2:
        return multiplyRange(range_sorted)

    if size > 2:
        first = range_sorted[size - 1]
        second = range_sorted[size - 2]
        third = range_sorted[size - 3]
        return multiplyRange([first, second, third])


def monk_multiplication(A, n):
    x = []
    z = -1
    for i in range(n):
        if i < 2:
            x.append(z)
        else:
            nums = find_numbers(A, 1, i)
            x.append(nums)
    return x


A = [1, 2, 3, 4, 5, 6, 7]
print(monk_multiplication(A, len(A)))
