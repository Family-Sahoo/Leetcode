def removeDuplicates(arr, n):
    temp = list(range(n))

    j = 0

    for i in range(n-1):
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1

    print("j: ", j, temp)
    temp[j] = arr[n-1]
    print("j: ", j, temp)
    j += 1
    print("j: ", j)

    for i in range(j):
        arr[i] = temp[i]

    print("arr", arr)

    return j

arr1 = [6,4,1,2, 1] #[1, 2, 2, 3, 4, 4, 4, 5, 5]
arr2 = sorted(arr1)
n = len(arr1)

jj = removeDuplicates(arr2, n)
print(jj)

for i in range(jj):
    print (f"{arr1[i]}", end = " ")    