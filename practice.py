import itertools
import functools

A = [3,8,4,6,2,1,9]

print(list(itertools.accumulate(A, lambda r,y: r+y)))
print(functools.reduce(lambda x,y: x+y, A))

def yieldfunc():
    yield 1
    yield 2
    yield 32


for i in yieldfunc():
    print(i)
