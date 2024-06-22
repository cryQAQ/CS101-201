model = list()
L = []
n = int(input())
for _ in range(n):
    m,d = input().split('-')
    if not m in model:
        model.append(m)
        L.append([m,[d]])
    else:
        L[model.index(m)][1].append(d)
L.sort(key=lambda x:x[0])
for i in L:
    a = i[1]
    amount = []
    for j in a:
        if j[-1] == 'B':
            amount.append([j,float(j[:-1]) * 1000])
        else:
            amount.append([j,float(j[:-1])])
    amount.sort(key=lambda x:x[1])
    i[1] = []
    for j in amount:
        i[1].append(j[0])
for i in L:
    print(i[0]+': '+', '.join(i[1]))