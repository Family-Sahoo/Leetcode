import sys
sys.setrecursionlimit(1000000)


def factorial(n):
    assert n >= 0 and n == int(n), 'Enter a positive integer'
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3.3))