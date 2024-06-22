import math
times = int(input())
for _ in range(times):
    l,k = map(int,input().split())
    L = [[[1]]]
    for i in range(l-1):
        L.append([])
        for j in range(math.factorial(i + 2)):
            for k in range(i + 2):
                L[i + 1].append(L[i][j].insert(k,i+2))