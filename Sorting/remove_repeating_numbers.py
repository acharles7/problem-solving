from collections import Counter

def removeRepeating(A, n):
    counter = Counter(A)
    print(counter)

    repeat = []
    for k, v in counter.items():
        if v >= n:
            repeat.append(k)
    print(repeat)

    for i in range(len(A)):
        if A[i] in repeat:
            A[i] = '$'
    print(A)
    output = []
    for i in A:
        if i != '$':
            print(i)
            output.append(i)
    print(output)

def removeRepeating2(A, k):
    for i in range(len(A)):
        


A = [3,1,2,2,2,1,1,1,2,2,3,1,1,2,2,2,1,1,1,2,3]
n = 3
removeRepeating(A, n)
