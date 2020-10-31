"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
"""


def isStrobogrammatic( num: str) -> bool: 
    numbers = {"1": "1", "0":"0", "8":"8", "6":"9", "9":"6"}
    output = ""
    for n in num:
        if n in numbers:
            output += numbers[n]
        else:
            return False
    return output[::-1] == num
