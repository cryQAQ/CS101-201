import math
N = int(input())
for i in range(N):
    n = int(input())
    L = []
    L.extend(input().split())
    for j in range(n):
        L[j] = int(L[j])
    G = []
    for j in range(n-1):
        G.append(L[j+1]-L[j])
    G.sort()
    if len(G) == 0:
        print(1)
    elif G[0]<0:
        print(0)
    elif G[0]%2 == 0:
        print(int(G[0]/2)+1)
    else:
        print(math.ceil(G[0]/2))