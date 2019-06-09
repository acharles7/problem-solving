#Check if two strings have a common substring

def two_string(a, b):
    flag = False
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                flag = True
                return flag
    return flag

a = 'chicken'
b = 'chilli'
print(two_string(a, b))
