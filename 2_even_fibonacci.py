import sys


def even_fib(x):
    s = []
    a,b = 0,1
    while a<x:
        if a%2==0:
            s.append(a)
        a,b = b,a+b
    return sum(s)

print(even_fib(int(sys.argv[1])))
