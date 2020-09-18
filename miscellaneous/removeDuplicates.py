'''
Given a string s, a k duplicate removal consists of choosing k adjacent
and equal letters from s and removing them causing the left and the 
right side  of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.
'''

def remove_duplicates(s, k):      
    stack = [1]
    out = s[0]

    for i in range(1, len(s)):
        if out and out[-1] == s[i]:
            stack[-1] += 1
        else:
            stack.append(1)

        out += s[i]

        if stack[-1] == k:
            stack.pop()
            out = out[:-k]
    return out


s = "deeedbbcccbdaa"
k = 3
remove_duplicates(s, k)

