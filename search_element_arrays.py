for el in ['a', 'b', 'x', 'y']:
    if el in ['z', 'x', 'y']:
        print(True) 
print()

d = {}
a1 = ['a', 1, ['x'], 'y']
b1 = ['z', 1, 'p', ['x']]

# print(set(a1) & set(b1))
# print(list(zip(sorted(a1), sorted(b1))))
# for i, j in zip(sorted(a1), sorted(b1)):
#     if i == j:
#         print(i)


for i in range(len(a1)):
    print(d.get(str(a1[i])))
    if d.get(str(a1[i])) is None:
        d[str(a1[i])] = True
print(d)

for i in range(len(b1)):
    if d.get(str(b1[i])):
        print(True)

print()

List1 = ['python', 'JS', 'c#', 'go', 'c', 'c++']
List2 = ['c#', 'Java', 'python']

check = any(item in List1 for item in List2)
check2 = all(item in List1 for item in List2)
print(check, check2)

List1.pop()
print(List1)
List1.append('Rust')
print(List1)

List1.extend(['Scala'])
print(List1)

List1.insert(5, 'HTML')
print(List1)