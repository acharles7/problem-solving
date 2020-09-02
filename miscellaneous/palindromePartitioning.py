'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
'''


def partition(s):
    
    def is_palindrome(s):
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def backtrack(s, index, temp, out):
        if index == len(s):
            out.append(temp)
            return
            
        for i in range(index, len(s)):
            temp_str = s[index:i+1]
            if is_palindrome(temp_str):
                backtrack(s, i+1, temp+[temp_str], out)
                
    out = []
    backtrack(s, 0, [], out)
    print(out)
    
s = "aab"
partition(s)

