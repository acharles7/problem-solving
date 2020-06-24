'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
'''

def addBinary(a: str, b: str) -> str:
    def getInt(a):
        out = 0
        for i, num in enumerate(reversed(a)):
            if num == '1':
                out += 2**i
        return out

    def getBinary(num):
        out = ''
        while num != 0:
            if num%2 == 0:
                out += str(0)
            else:
                out += str(1)
            num = num//2
        return out[::-1]

    out = getBinary(getInt(a) + getInt(b))
    return out if out else '0'

def addBinary(a: str, b: str) -> str:
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)

    carry = 0
    out = []

    for i in range(n-1, -1, -1):
        if a[i] == '1':
            carry += 1

        if b[i] == '1':
            carry += 1

        if carry%2 == 1:
            out.append('1')
        else:
            out.append('0')
        carry //= 2

    if carry == 1:
        out.append('1')

    return ''.join(out[::-1])
