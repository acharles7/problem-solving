# the degree of this array is defined as the maximum frequency of any
# one of its elements.

# find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.


def findShortestSubArray(A):
    left, right, count = {}, {}, {}
    for i, x in enumerate(A):
        if x not in left:
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    degree = len(A)
    length = max(count.values())

    for x in count:
        if count[x] == length:
            degree = min(degree, right[x] - left[x] + 1)
    return degree


A = [2, 5, 1, 2, 1, 2, 3, 1]
print(findShortestSubArray(A))
