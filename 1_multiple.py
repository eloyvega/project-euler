import sys


def get_sum_multiples(x):
    return sum([n for n in range(1,x) if n%3==0 or n%5==0])

print(get_sum_multiples(int(sys.argv[1])))
