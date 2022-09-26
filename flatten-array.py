def flatten_arr(arr):
    flat_arr = []
    
    
    for elements in arr:
        if type(elements) is list:
            flat_arr.extend(flatten_arr(elements))
        else:
            flat_arr.append(elements)

    return flat_arr

arr = [1, 2, [3]] # , [4, [5, [6, [7, [8, [9]]]]]]]]
print(flatten_arr(arr))

