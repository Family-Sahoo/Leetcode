""" Add 1 to the array
initial_array = [1, 2, 4, 5]
final_array = [1, 2, 4, 6]

initial_array = [1, 9, 9]
final_array = [2, 0, 0]

initial_array = [9, 9]
final_array = [1, 0, 0]
"""
from typing import final


initial_array = [0, 0, 0]

carry = 1
final_arr = [0 for i in range(len(initial_array))]

for i in range(len(initial_array)-1, -1, -1):
    print(i)
    sum = initial_array[i] + carry

    if sum == 10:
        final_arr[i] = 0
        carry = 1 
    else:
        final_arr[i] = initial_array[i] + carry
        carry = 0

if carry == 1:
    final_arr.insert(0, 1)

print(final_arr)   

## 2

initial_array = [0, 0, 0]

new_arr = [str(x) for x in initial_array ]
s = str(int(''.join(new_arr)) + 1 )
print(type(s))

initial_array = s.split()
print(initial_array)

## 3
digits = [1, 9, 9]


result = map(str, digits)
print(result)

result = "".join(result)
print(result, type(result))
result = int(result) + 1
result = list(map(int, str(result)))

