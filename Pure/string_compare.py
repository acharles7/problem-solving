import string

alphabets = list(string.ascii_lowercase)  # list of alphabets, ['a', 'b', ..., 'z']

def compare(a, b):
    i = 0
    while i < len(a):
        i += 1
        letter1 = a[i]
        letter2 = b[i]
        if alphabets.index(letter1) > alphabets.index(letter2):
            return 1
        elif alphabets.index(letter2) > alphabets.index(letter1):
            return 0
    return -1

def compare2(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

# print(compare('abcabc', 'bbbaaa'))  # True   ['bbbaaa', 'abcabc']
# print(compare('xxx', 'zzz'))        # False  ['xxx', 'zzz']
# print(compare('abc', 'abcd'))     # Error

from functools import cmp_to_key
x = sorted([('zaaaaa', 'bbbaaa')], key=cmp_to_key(compare))
# x = sorted([('zzzacabc', 'bbbaaacc')], key=lambda l: compare2)
print(x)
