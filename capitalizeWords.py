from cgitb import reset


def capitalizeWords(arr):
    cap_arr = []
    if len(arr) == 0:
        return cap_arr
    # for item in arr:
    #     cap_arr.append(item.upper())
    # return cap_arr
    cap_arr.append(arr[0].upper())
    return cap_arr + capitalizeWords(arr[1:])

print(capitalizeWords(['i', 'am', 'learning', 'recursion']))