# Find the element that appears once in a sorted array
# Time Complexity: O(log n)


def find_that_element(A, low, high):
    if low > high:
        return None

    if low == high:
        return A[low]

    mid = (low + high) // 2

    if mid % 2 == 0:
        if A[mid] == A[mid + 1]:
            return find_that_element(A, mid + 2, high)
        else:
            return find_that_element(A, low, mid)
    else:
        if A[mid] == A[mid - 1]:
            return find_that_element(A, mid + 1, high)
        else:
            return find_that_element(A, low, mid - 1)


A = [1, 1, 2, 2, 3, 4, 4, 5, 5]
element = find_that_element(A, 0, len(A) - 1)
print(element)
