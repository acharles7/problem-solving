def minimumTime(files):

    files.sort()

    time = files[0]
    output = []

    for i in range(1, len(files)):
        time += files[i]
        output.append(time)
    print(output)
    return sum(output)

def minimumTime2(files):
    files.sort()
    print(files)
    output = []
    l, r = 0, len(files) - 1
    while(l < r):
        time = files[l] + files[r]
        output.append(time)
        l += 1
        r -= 1
    print(output)
    return sum(output)
files = [20, 4, 8, 2]
print(minimumTime2(files))
# print(minimumTime(files))
