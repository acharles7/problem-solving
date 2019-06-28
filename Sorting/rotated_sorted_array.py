# Search in Rotated Sorted Array

def findIndex(nums,l, r):
    if nums[l] < nums[r]:
        return 0
    while l <= r:
        mid = (l + r) // 2
        if(nums[mid] > nums[mid + 1]):
            return mid + 1

        if(nums[mid] < nums[l]):
            r = mid - 1
        else:
            l = mid + 1

def binarySearch(nums, l, r, target):
    while(l <= r):
        mid = (l + r) // 2
        if(target == nums[mid]):
            return mid
        if(target < nums[mid]):
            r = mid - 1
        else:
            l = mid + 1
    return -1


def search(nums, target):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if(nums[0] == target):
            return 0
        return -1

    rindex = findIndex(nums, 0, len(nums) - 1)

    if rindex == 0:
        return binarySearch(nums, 0, len(nums) - 1, target)
    if nums[rindex] == target:
        return rindex
    if target < nums[0]:
        return binarySearch(nums, rindex, len(nums) - 1, target)
    return binarySearch(nums, 0, rindex, target)

A = [4,5,6,7,8,1,2,3]
target = 6
print(search(A, 6))
