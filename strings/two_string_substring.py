#Check if two strings have a common substring

#Time Complexity: O(nˆ2)
def two_string(a, b):
    flag = False
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                flag = True
                return flag
    return flag

#Time Complexity: O(n)
def two_string_n(a, b):
    v = [0] * 26
    flag = False
    for i in a:
        v[ord(i) - ord('a')] += 1
    for j in b:
        if(v[ord(j) - ord('a')] >= 1):
            flag = True
            return flag
    return flag

a = 'chicken'
b = 'jkl'
print(two_string(a, b))
print(two_string_n(a, b))
