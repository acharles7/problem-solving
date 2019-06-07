#Find element which occurs thrice in an array in O(n)

def thrice_occuring(A):
    return abs(2 * sum(set(A)) - sum(A))

A = [2,3,4,5,7,9,4,3,2,5,7,9,3]
element = thrice_occuring(A)
print(element)
