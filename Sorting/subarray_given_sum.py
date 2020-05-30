def subArraySum(A, k):
    dic = {}
    curr_sum = 0

    for i in range(len(A)):
        curr_sum += A[i]
        print(dic, curr_sum)
        if curr_sum == k:
            return [0, i]
        print(curr_sum - k)
        if curr_sum - k in dic:
            return [dic[curr_sum - k] + 1, i]
        else:
            dic[curr_sum] = i


A = [1, 4, 20, 3, 10, 5]
k = 33
print(subArraySum(A, k))
