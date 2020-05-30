# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.


def searchInsert(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
        if target < num:
            return i
    return len(nums)


A = [2, 4, 50, 55, 60, 93]
target = 3
print(searchInsert(A, target))
