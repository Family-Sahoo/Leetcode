def CapitalizeFirst(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr[0].capitalize()]
    else:
        return [arr[0].capitalize()] + (CapitalizeFirst(arr[1:]))

print(CapitalizeFirst(['bus', 'train']))
