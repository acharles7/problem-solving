'''
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
'''

def simplifyPath(path: str) -> str:
    stack = []
    dirs = path.split('/')

    for token in dirs:
        if token == '' or token == '.':
            continue
        elif token == '..':
            if stack:
                stack.pop()    
        else:
            stack.append(token)
    if stack:
        return '/'+'/'.join(stack)
    return '/'

print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/a/./b/../../c/"))
print(simplifyPath("/a/../../b/../c//.//"))
print(simplifyPath("/a//b////c/d//././/.."))
