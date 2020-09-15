'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''

# Time O(n), Space O(n)
def find_duplicates(nums):   
    visited = set()
    output = []

    for num in nums:
        if num in visited:
            output.append(num)
        visited.add(num)
    return output


# Time O(n)
def find_duplicates2(nums):
    out = []
    for num in nums:
        if nums[abs(num)-1] < 0:
            out.append(abs(num))
        nums[abs(num)-1] *= -1
    return output

nums = [4,2,7,8,2,3,1, 8]
find_duplicates2(nums)
