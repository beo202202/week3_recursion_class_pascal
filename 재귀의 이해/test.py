import sys

def recursion(n):
    print(n)
    recursion(n+1)

# recursion(1)
print(sys.getrecursionlimit())