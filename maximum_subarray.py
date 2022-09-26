from array import array


input = [1, -4, 2, 5, -1, 9]

maximum = max_arr = input[0]

for i in range(1, len(input)):
    max_arr = max(input[i], max_arr+input[i])
    maximum = max(max_arr, maximum)

print(maximum)
