# remove two adjacent duplicates from string recursively.

def removeDuplicates(s):
    output = []

    for char in s:
        if len(output) > 0 and char == output[-1]:
            output.pop()
        else:
            output.append(char)
    return ''.join(output)

s = "dabbadca"
print(removeDuplicates(s))
