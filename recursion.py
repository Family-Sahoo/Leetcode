def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n*n)

recursiveMethod(4)
print()

def powerofTwo(n):
    if n == 0:
        return 1
    else:
        return  2 * powerofTwo(n-1)

a = powerofTwo(5)
print("Result: ", a)
