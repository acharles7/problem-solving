
def fullJustify(words, width):
    length = []
    for i in words:
        length.append(len(i))
    print(length)

    output = []
    line = []
    cnt = 0
    for i in range(len(length)):
        cnt += length[i]
        if cnt < width:
            line.append(words[i])
        output.append(line)
        cnt = 0

        print(line)

    print(output)

words = ["This", "is", "an", "example", "of", "text", "justification."]
width = 16
fullJustify(words, width)
