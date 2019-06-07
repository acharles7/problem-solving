#Given a string, find its first non-repeating character

#Time Complexity: O(1)
def non_repeat_char_linear_time(stream):
    repeated = [False] * 256
    DLL = []

    for char in stream:
        if not repeated[ord(char)]:
            if char not in DLL:
                DLL.append(char)
            else:
                DLL.remove(char)
    return DLL[0]

#Time Complexity: O(n)
def non_repeat_char(stream):
    counter = {}
    for char in stream:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    for k,v in counter.items():
        if(v == 1):
            return k

stream = 'happybirthdaybossie'
print(non_repeat_char(stream))
print(non_repeat_char_linear_time(stream))
