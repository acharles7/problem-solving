# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value


def searchRange(nums, target):
    if len(nums) < 1:
        return -1, -1

    left, right = -1, -1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    if nums[l] != target:
        return -1, -1

    left = l
    l, r = left, len(nums) - 1
    while l < r:
        mid = (l + r) // 2 + 1
        if nums[mid] == target:
            l = mid
        else:
            r = mid - 1
    right = l
    return left, right


A = [5, 7, 7, 8, 8, 8, 9, 10]
target = 8
print(searchRange(A, target))
