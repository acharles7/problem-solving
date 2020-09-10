'''
Given a string s and a non-empty string p, 
find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the 
length of both strings s and p will not be larger than 20,100. 
The order of output does not matter.
'''

def findAnagrams(self, s: str, p: str) -> List[int]:   
        
    ps, ss, out = [0]*26, [0]*26, []
    p_len = len(p)

    for char in p:
        ps[ord(char)-ord('a')] += 1

    for i in range(len(s)):
        ss[ord(s[i])-ord('a')] += 1

        if i >= p_len:
            ss[ord(s[i-p_len])-ord('a')] -= 1

        if ss == ps:
            out.append(i-p_len+1)
    return out
    
