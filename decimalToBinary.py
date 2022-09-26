def decimalToBinary(decimal_num):
    assert decimal_num >= 0 and decimal_num == int(decimal_num), "Enter a positive integer"
    if decimal_num == 0:
        return decimal_num
    else:
        return decimal_num % 2 + 10 * decimalToBinary(decimal_num // 2)

print(decimalToBinary(11))