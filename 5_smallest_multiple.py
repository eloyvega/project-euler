import math
import sys


number = int(sys.argv[1])
n = math.factorial(number)

for i in range(2, number+1):
    divide = True
    while n%i == 0 and divide:
        aux = n/i
        for k in range(2,number+1):
            if aux%k != 0:
                divide = False
                break
        if divide:
            n = aux

print(n)
