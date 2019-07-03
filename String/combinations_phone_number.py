def letterCombinations(digits: str):
    nums = [[2, 'abc'],[3, 'def'],[4, 'ghi'],[5, 'jkl'], [6, 'mno'], [7, 'pqrs'], [8, 'tuv'], [9, 'wxyz']]
    out = []
    combi = []
    jump = []

    if len(digits) <= 0:
        return []

    for i in range(len(digits)):
        for j in range(len(nums)):
            if(nums[j][0] == int(digits[i])):
                combi.append(nums[j][1])
                jump.append(len(nums[j][1]))
    length = 1
    for i in combi:
        length *= len(i)

    times = []
    div = jump[0]
    times.append(length//div)

    for i in range(1,len(jump)):
        div *= jump[i]
        times.append(length//div)

    p = 0
    while(p < length):
        for i in combi[0]:
            for k in range(times[0]):
                out.append(i)
                p += 1
                
    for i in range(1, len(combi)):
        q = 0
        while(q < length):
            for j in combi[i]:
                for k in range(times[i]):
                    out[q] += j
                    q += 1
    return out


digits = "5678"
print(letterCombinations(digits))
