## 1
inputy = [0, 1, 2, 0, 4]

for i in range(len(inputy)): #O(n)
    if inputy[i] == 0:
        inputy.remove(inputy[i]) #O(n)
        inputy.append(0)
print(inputy)        #O(n^2)

## 2

a = [1, 0, 1, 0, 63, 12, 0, 1, 5]

z = 0
for i in range(len(a)):
    if a[i] != 0:
        a[i], a[z] = a[z], a[i]
        z += 1

print(a)        #O(n)

## 3
a = [1, 0, 1, 0, 63, 12, 0, 1, 5]
print("Before operation: ", a)
a.sort(key=bool, reverse=True)
print("After operation: ", a) #O(nlogn)