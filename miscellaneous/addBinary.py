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
