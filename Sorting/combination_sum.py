# find all unique combinations in candidates where the candidate numbers sums to target.

def combinationSum(candidates, target):
    def findNumbers(candidates, target, res, start):
        if target == 0:
            return output.append(res)

        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            findNumbers(candidates, target - candidates[i], res + [candidates[i]], i)

    candidates.sort()
    output = []
    findNumbers(candidates, target, [], 0)
    return output

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))
