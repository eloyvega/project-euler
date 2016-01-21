import sys
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

# My answer
def largest_prime_factor_mine(x):
    for i in range(1,x+1):
        if x%i==0 and is_prime(x//i):
            return x//i

# The answer
def largest_prime_factor(n):
    if n % 2 == 0:
        n = n/2
        last_factor = 2
        while n % 2 == 0:
            n = n/2
    else:
        last_factor = 1
    factor = 3
    max_factor = math.sqrt(n)
    while n > 1 and factor <= max_factor:
        if n%factor == 0:
            last_factor = factor
            n = n/factor
            while n % factor == 0:
                n = n/factor
            max_factor = math.sqrt(n)
        factor += 2
    if n == 1:
        return last_factor
    else:
        return int(n)

print(largest_prime_factor(int(sys.argv[1])))
