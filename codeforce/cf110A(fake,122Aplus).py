n = input()
L = []
for i in range(len(n)):
    L.append([])
L[0].append(4)
L[0].append(7)
for i in range(1,len(n)):
    for j in range(len(L[i-1])):
        L[i].append(L[i-1][j]*10+4)
        L[i].append(L[i-1][j]*10+7)
a = 0
for i in range(len(n)):
    for j in range(len(L[i])):
        if int(n)%L[i][j] == 0:
            print('YES')
            a += 1
        break
if a == 0:
    print('NO')
print(L)
#可以看见如何使用二维列表