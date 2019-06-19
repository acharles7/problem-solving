#two sum

def two_sum(A, target):
    dic = {}
    for i, num in enumerate(A):
        n = target - num
        if(n not in dic):
            dic[num] = i
        else:
            return [A[dic[n]],A[i]]

def two_sum_2(arr, target):
    A.sort()
    l, r = 0, len(A) - 1
    while(l < r):
        sum = A[l] + A[r]
        if(sum == target):
            return [A[l],A[r]]
        elif (sum < target):
            l += 1
        else:
            r -= 1
    return False

A = [4,6,1,9,0,5,3]
target = 8
print(two_sum(A, target))
print(two_sum_2(A, target))
