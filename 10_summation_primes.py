import sys
import math


def is_prime(n):
    if n ==1: return False
    elif n < 4: return True
    elif n%2 == 0: return False
    elif n<9: return True
    elif n%3 == 0: return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f<=r:
            if n%f ==0: return False
            if n%(f+2)==0: return False
            f += 6
        return True

def sum_primes(n):
    return sum([x for x in range(2,n) if is_prime(x)])

print(sum_primes(int(sys.argv[1])))
