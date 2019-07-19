def encode(strs):
    if strs is None:
        return ""
    numb = ""
    for s in strs:
        if not s:
            numb += " "
        for c in s:
            numb += str(ord(c))
            numb += ':'
        numb += '-'
    return numb[:-1]

def decode(s):
    if not s:
        return []
    strs = s.split('-')
    output = []
    for st in strs:
        each = ""
        nums = st.split(':')[:-1]
        for c in range(len(nums)):
            each += chr(int(nums[c]))
        output.append(each)
    return output


strs = ['hello', 'world', 'better']
print(decode(encode(strs)))
