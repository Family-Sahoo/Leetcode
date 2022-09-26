s = 'abc'
ss = list(s)
print("ss: ", ss)
t = []
for i in range(len(s)-1, -1, -1):
    t.append(s[i])   
print("After joined: ", ''.join(t))    

k = reversed(ss)
print(list(k))

ss.reverse()
print(''.join(ss))

s = 'a'
print(len(s))