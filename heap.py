def Heapify(array, n, i):
    larg = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and array[i]< array[l]:
        larg = l

    if r < n and array[larg] < array[r]:
        larg = r

    if larg != i:
        array[larg],array[i] = array[i],array[larg]
        Heapify(array,n,larg)


def HeapSort(array,n):
    for i in range(n, -1, -1):
        Heapify(array, n, i)

    for i  in range(n-1, -1, -1):
        array[i],array[0] = array[0],array[i]
        Heapify(array, i, 0)



array = [1,3,2,9,5,4,8,22,19,56,34,31]
n = len(array)
HeapSort(array,n)

print("Sorted Array")

for i in range(n):
    print("%d" %array[i])
