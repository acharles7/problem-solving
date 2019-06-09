#Check if a string is substring of another

def check_substring(a, b):
    for i in range(len(a) - len(b) + 1):
        if(a[i:i+len(b)] == b):
            return i
    return 0

a = 'chickenchilli'
b = 'chilli'
print(check_substring(a, b))
