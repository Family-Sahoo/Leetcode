def sumOfDigits(n):
    assert n >= 0 and n == int(n), "Enter a positive integer"


    divisor, remainder = n // 10, n % 10
    # print(divisor, remainder)
    if n == 0:
        return 0
    else:
        return remainder + sumOfDigits(divisor)

print(sumOfDigits(111))
