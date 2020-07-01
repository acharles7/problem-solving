'''
You are given an integer array nums and you have to return a new
counts array. The counts array has the property where counts[i] 
is the number of smaller elements to the right of nums[i].
'''

def countSmaller(nums: List[int]) -> List[int]:
    out = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                count += 1
        out.append(count)
    return out
