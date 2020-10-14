"""
Given a VPS(valid parentheses string) represented as string s, 
return the nesting depth of s.
"""

def max_depth(s: str) -> int:
    stack, max_depth = [], 0
    
    for char in s:
        max_depth = max(max_depth, len(stack))
        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()
    return max_depth


assert max_depth("(1+(2*3)+((8)/4))+1") == 3
assert max_depth("(1)+((2))+(((3)))") == 3
assert max_depth("1+(2*3)/(2-1)") == 1
assert max_depth("1") == 0

