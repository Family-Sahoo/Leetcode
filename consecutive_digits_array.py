"""Question was as follows :

Given an array find the minimum amount of values to add to make the array consecutively increasing or consecutively decreasing
Example: input array = [5, 7, 9, 4, 11]
Add 2 to 5
Add 1 to 7
Add 6 to 4
Now the array is consecutively increasing ([7, 8, 9, 10, 11]). The total amount that was added is 2 + 1 + 6 = 9 so return 9
Can anyone give a solution or a link to a very similar problem?
"""

def min_additions(arr):
    last = arr[-1]
    diff = 0
    for i in range(len(arr)-2, -1, -1):
        if last > arr[i]:
            diff = last - arr[i] - 1
            arr[i] += diff
            last = arr[i]
        elif last < arr[i]:
            diff = arr[i] - last - 1
            arr[i] -= diff
            last = arr[i]
        else:
            diff = 0
            last = arr[i]
    print(arr)
    


print(min_additions([6, 3, 2]))