def get_split_point(A):
    for i in range(len(A)-1):
        if(A[i] - A[i+1] > 0):
            return i+1
def sorted_array(A):
    split = get_split_point(A)
    split_before = A[0:split]
    split_after = A[split:len(A)]
    X = split_after + split_before
    return X

A = [2, 3, 4, 0, 1, 2]
print(sorted_array(A))
