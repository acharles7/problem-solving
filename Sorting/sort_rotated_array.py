# Sort a Rotated Sorted Array

# Get the split point using Iterative method
def get_split_point(A):
    for i in range(len(A) - 1):
        if A[i] - A[i + 1] > 0:
            return i + 1


# Get the split point using Binary Search Method
def get_split_point_BST(A, low, high):
    if low > high:
        return -1
    if low == high:
        return low
    mid = (low + high) // 2

    if A[mid] > A[mid + 1]:
        return mid + 1
    if A[mid] < A[mid - 1]:
        return mid
    if A[low] < A[high]:
        return get_split_point_BST(A, low, mid - 1)
    else:
        return get_split_point_BST(A, mid + 1, high)


def sorted_array(A):
    # split = get_split_point(A)
    split = get_split_point_BST(A, 0, len(A))
    split_before = A[0:split]
    split_after = A[split : len(A)]
    X = split_after + split_before
    return X


A = [12, 23, 24, 0, 2, 10]
print(sorted_array(A))
