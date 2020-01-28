'''
Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
The only constraint stopping you from robbing each of them is that adjacent houses
have security system connected and it will automatically contact the police if two
adjacent houses were broken into on the same night.
'''

def rob(nums) -> int:
    prev_max = 0
    curr_max = 0
    for num in nums:
        temp = curr_max
        curr_max = max(curr_max, prev_max + num)
        prev_max = temp
    return curr_max

nums = [2,7,9,3,1]
print(rob(nums))
