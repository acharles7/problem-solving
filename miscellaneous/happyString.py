'''
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at 
most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".
'''

def longestDiverseString(a: int, b: int, c: int) -> str:    
    out = ''
    alphas = {'a': a, 'b': b, 'c': c}
    previous = None
    while True:
        count1, char1 = max((alphas[char], char) for char in ('a','b', 'c'))
        count2, char2 = max((alphas[char], char) for char in ('a','b', 'c') if char != char1)

        if not count1: break
        char1_max = 1 if previous == char1 else 2
        char1_max = min(char1_max, count1)
        out += char1*char1_max
        alphas[char1] -= char1_max

        if count2:
            out += char2
            alphas[char2] -= 1
        else:
            break
        previous = char2

    return out

