'''
Output an array with values made up of indices of the element with 
value greater than the current element but with largest index.
'''

def get_indices(nums):
    out = []
    for i in range(len(nums)):
        max_index = -1
        flag = False
        for j in range(len(nums)-1, i, -1):
            if nums[i] < nums[j]:
                flag = True
                out.append(j)
                break
        if not flag:    
            out.append(-1)
    return out  
        
nums = [1,20,21,5,9,10,15]
print(get_indices(nums))
