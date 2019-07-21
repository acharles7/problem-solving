# Algoritm to find minimum possible time to merge N subfiles into a single file

def minimumTime(files):
    files.sort()

    time = files[0]
    output = []
    for i in range(1, len(files)):
        time += files[i]
        output.append(time)
    return sum(output)

# Optimal
def minimumTime2(files):
    files.sort()

    output = []
    l, r = 0, len(files) - 1
    while(l < r):
        time = files[l] + files[r]
        output.append(time)
        l += 1
        r -= 1
    return sum(output)
files = [1, 2, 5, 10, 35, 89]

print("Optimal:", minimumTime2(files))
print("Less Optimal:", minimumTime(files))
