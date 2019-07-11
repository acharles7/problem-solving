def findNumber(candies, people):
    res = [0] * people

    candy = 1
    i = 0

    while(candies):
        print(res)
        given = min(candy, candies)
        res[i] += given
        candies -= given
        i = (i + 1) % people
        candy += 1
    return res

candies = 7
people = 4
print(findNumber(candies,people))
