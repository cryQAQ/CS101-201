m,n,p,q = map(int,input().split())
A,B,C = [],[],[[] for _ in range(m + 1 - p)]
for _ in range(m):
    A.append(list(map(int,input().split())))
for _ in range(p):
    B.append(list(map(int,input().split())))
for i in range(m + 1 - p):
    for j in range(n + 1 - q):
        c = 0
        for k in range(p):
            for l in range(q):
                c += A[i + k][j + l] * B[k][l]
        C[i].append(c)
    print(' '.join(map(str,C[i])))