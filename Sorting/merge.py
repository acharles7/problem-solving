
def mergeSort(array, l, r):
    if l < r :
        m = int(l + (r-1)) // 2
        mergeSort(array, l, m)
        mergeSort(array, m+1, r)
        merge(array, l, m, r)

def merge(array, l, m, r):

    n1 = int(m-l+1)
    n2 = int(r-m)
    left_array = [0] *n1
    right_array = [0] *n2

    for i in range(n1):
        left_array[i] = array[l+i]
    for i in range(n2):
        right_array[i] = array[m + 1 + i]

    i = l
    l_ptr = 0
    r_ptr = 0

    while i != r+1 :
        if left_array[l_ptr] < right_array[r_ptr]:
            array[i] = left_array[l_ptr]
            l_ptr = l_ptr+1
            i = i+1

            if l_ptr >= n1:
                while(i != r+1):
                    array[i] = right_array[r_ptr]
                    i = i+1
                    r_ptr = r_ptr+1
        else:
            array[i] = right_array[r_ptr]
            r_ptr = r_ptr+1
            i = i+1

            if r_ptr >= n2:
                while i != r+1:
                    array[i] = left_array[l_ptr]
                    i+=1
                    l_ptr+=1

    print(array)
# Main Function
array = [6,2,7,3,9,4]
n = len(array)
start = 0
end = int(len(array)-1)
mergeSort(array, start, end)
print(array)
