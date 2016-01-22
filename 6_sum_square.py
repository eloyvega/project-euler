import sys


n = int(sys.argv[1])
result = sum(range(1,n+1))**2 - sum([x**2 for x in range(1,n+1)])
print(result)
