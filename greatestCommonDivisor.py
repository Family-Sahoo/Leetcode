def greatestCommonDivisor(num1, num2):
    assert num1 == int(num1) and num2 == int(num2), "Enter a positive integer"
    if num1 < 0:
        num1 *= -1
    if num2 < 0:
        num2 *= -1    

    if num2 == 0:
        return num1
    else:
        return greatestCommonDivisor(num2, num1 % num2)


print(greatestCommonDivisor(-18, 48))