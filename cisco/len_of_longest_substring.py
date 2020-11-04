"""
Given a string s, find the length of the longest substring without repeating characters.
"""

def length_of_longest_substring(s: str) -> int:
    l, r, maximum = 0, 0, 1
    temp = set()

    if not s: return 0

    while r < len(s):
        if s[r] not in temp:
            temp.add(s[r])
            r += 1
            maximum = max(maximum, r-l)
        else:
            temp.remove(s[l])
            l += 1
    return maximum
                  
    
s = "abcabcbb"
length_of_longest_substring(s)

