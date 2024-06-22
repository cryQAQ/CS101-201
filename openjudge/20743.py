s = input()
L = [[]]
for i in s:
    if i == '(':
        L.append([])
    elif i == ')':
        a = L.pop()
        L[-1] += a[::-1]
    else:
        L[-1].append(i)
print(''.join(L[0]))