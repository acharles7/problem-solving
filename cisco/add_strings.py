"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
"""

def addStrings(num1: str, num2: str) -> str:
    res = []
    carry = 0

    n = len(num1)-1
    m = len(num2)-1

    while n >= 0 or m >= 0:
        x = ord(num1[n])-ord('0') if n >= 0 else 0
        y = ord(num2[m])-ord('0') if m >= 0 else 0

        carry, value = divmod(x + y + carry, 10)

        res.append(value)

        n -= 1
        m -= 1

    if carry:
        res.append(carry)

    return ''.join(map(str, res[::-1]))

