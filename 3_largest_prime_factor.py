import sys
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def largest_prime_factor(x):
    for i in range(1,x+1):
        if x%i==0 and is_prime(x//i):
            return x//i

print(largest_prime_factor(int(sys.argv[1])))
