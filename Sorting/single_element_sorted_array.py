# Given a sorted array consisting of only integers where every element appears
# exactly twice except for one element which appears exactly once.
# Find this single element that appears only once.


def singleNonDuplicate(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if mid % 2 == 0:
            if nums[mid] == nums[mid + 1]:
                l += 2
            else:
                r = mid
        else:
            if nums[mid] == nums[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return nums[l]


nums = [0, 1, 1, 3, 3, 4, 4, 8, 8]
print(singleNonDuplicate(nums))
