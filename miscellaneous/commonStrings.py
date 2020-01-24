def commonSubstring(A, B):
    output = []
    for a, b in zip(A, B):
        counterA = [0]*26
        counterB = [0]*26
        isCommon = False

        for l in a:
            counterA[ord(l)-ord('a')] += 1
        for l in b:
            counterB[ord(l)-ord('a')] += 1

        for l1, l2 in zip(counterA, counterB):
            if l1 >=1 and l2 >= 1:
                isCommon = True
                break
        if isCommon:
            output.append('YES')
        else:
            output.append('NO')
    return output

A = ['hell', 'hi', 'asd', 'sqw']
B = ['world', 'bye', 'fgh', 'qwe']
print(commonSubstring(A, B))
