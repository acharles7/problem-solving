def two_sum(A, target):
    dic = {}
    for i, num in enumerate(A):
        n = target - num
        if(n not in dic):
            dic[num] = i
        else:
            return [dic[n],i]

A = [4,6,1,9,0,5,3]
target = 8
print(two_sum(A, target))
