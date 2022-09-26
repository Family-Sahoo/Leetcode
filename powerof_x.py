def powerOfX(n, exp):
    assert exp >= 0 and exp == int(exp), "Enter a positive integer"

    if exp == 0:
        return 1
    if exp == 1:
        return n
    else:
        return n * powerOfX(n, exp-1)

print(powerOfX(-5.5, 6))