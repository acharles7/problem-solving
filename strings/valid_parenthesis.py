# Valid Parenthesis

def isValid(s):
    stack = []
    braces = {'{':'}','[':']','(':')'}
    for i in s:
        if i in braces:
            stack.append(i)
        else:
            if stack:
                top = stack.pop()
            else:
                top = '#'
            if braces[top] != i:
                return False
    return not stack

s = "{[]}"
print(isValid(s))
