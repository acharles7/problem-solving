
def twoSum(nums, target):
    answer, nums = set(), set(nums)
    for num in nums:
        comp = target - num
        if comp in nums:
            if num > comp:
                res = (num, comp)
            else:
                res = (comp, num)
            if res not in answer:
                answer.add(res)
    return (answer, len(answer))


nums = [1, 1, 2, 2]
target = 3
print(twoSum(nums, target))
