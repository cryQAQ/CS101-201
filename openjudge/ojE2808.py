L,M = map(int,input().split())
n = set()
for i in range(0,L+1):
    n.add(i)
for i in range(M):
    S,E  = map(int,input().split())
    for j in range(S,E+1):
        if j in n:
            n.remove(j)
print(len(n))