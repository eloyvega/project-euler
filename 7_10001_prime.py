import sys
import math


# answer implementation:
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

def get_prime(n):
    if n == 1:
        return 2
    i = 1
    c = 1
    while c<n:
        i += 2
        if is_prime(i):
            c +=1
    return i


print(get_prime(int(sys.argv[1])))
