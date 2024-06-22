n,k = map(int,input().split())
L = sorted(list(map(int,input().split())))
if k == n:
    print(L[-1])
elif k == 0 and L[0] > 1:
    print(1)
elif k == 0 and L[0] == 1:
    print(-1)
elif L[k - 1] == L[k]:
    print(-1)
else:
    print(L[k - 1])