# Given a string S, find out the length of the longest repeating substring(s). 
# Return 0 if no repeating substring exists.

def longestRepeatingSubstring(S):
    length = 0
    for i in range(len(S)):
        j = i + 1
        while j < len(S) and j + length < len(S):
            if(S[i:i+length+1] == S[j:j+length+1]):
                length += 1
            else:
                j += 1
    return length

S = "aabcaabdaab"
print(longestRepeatingSubstring(S))
