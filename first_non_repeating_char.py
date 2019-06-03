#Given a string, find its first non-repeating character
#Time Complexity: O(n)

def non_repeat_char(S):
    counter = {}
    for char in S:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    for k,v in counter.items():
        if(v == 1):
            return k

S = 'happybirthday'
print(non_repeat_char(S))
