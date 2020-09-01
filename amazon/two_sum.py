
def twoSum(nums, target):
    answer, complement = set(), set()
    for num in nums:
        comp = target - num
        if comp in complement:
            if num > comp:
                res = (num, comp)
            else:
                res = (comp, num)
            if res not in answer:
                answer.add(res)
        complement.add(num)
    return (answer, len(answer))

nums = [0,4,1,6,2,9,3,5,1,7]
target = 6
print(twoSum(nums, target))
