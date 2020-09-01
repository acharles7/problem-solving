# Given a string, sort it in decreasing order based on the frequency of characters.

from collections import Counter
def frequencySort(s):
    res = ""
    for k, v in sorted(Counter(s).items(), reverse = True, key = lambda p: p[1]):
        res += k*v
    return res
s = "Robinhood"
print(frequencySort(s))
