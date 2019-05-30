def multiplyList(M):
    mul = 1
    for ele in M:
        mul = mul * ele
    return mul

def find_numbers(A, start, end):
    range = A[start:end+1]
    range_sorted = sorted(range)

    if(len(range_sorted) == 2):
        return multiplyList(range_sorted)

    if(len(range_sorted) > 2):
        temp = []
        last_index = len(range_sorted) - 1
        first = range_sorted[last_index]
        second = range_sorted[last_index-1]
        third = range_sorted[last_index-2]
        temp = [first, second, third]
        return multiplyList(temp)

def monk_multiplication(A, n):
    x = []
    z = -1
    for i in range(n):
        if(i < 2):
            x.append(z)
        else:
            nums = find_numbers(A, 1, i)
            x.append(nums)
    print(x)

A = [1,2,3,4,5,6,7]
monk_multiplication(A, len(A))
