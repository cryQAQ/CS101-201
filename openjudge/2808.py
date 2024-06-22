L,M = map(int,input().split())
l = [1] * (L + 1)
for _ in range(M):
    s,e = map(int,input().split())
    for i in range(s,e + 1):
        l[i] = 0
print(sum(l))