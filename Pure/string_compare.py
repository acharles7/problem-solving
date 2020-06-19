import string

alphabets = list(string.ascii_lowercase)  # list of alphabets,['a', 'b'.., 'z']

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

# print(compare('abcabc', 'bbbaaa'))  # True   ['bbbaaa', 'abcabc']
# print(compare('xxx', 'zzz'))        # False  ['xxx', 'zzz']
# print(compare('abc', 'abcd'))       # Error
