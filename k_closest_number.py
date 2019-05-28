#Given an unsorted array and two numbers x and k, find k closest values to x.
#Time Complexity:  O(n + k)

def func(ele):
    return ele[1]
def k_closest(A, n, k):
    x = []
    closest = []
    for i in range(len(A)):
        diff = abs(n - A[i])
        temp = [A[i], diff]
        x.append(temp)
    A_sorted = sorted(x, key=func, reverse=False)
    for i in range(k):
        closest.append(A_sorted[i][0])
    return closest

A = [-10, -50, 20, 17, 80]
n = 20
k = 2
print("Kth_Closest: ",k_closest(A, n, k))
