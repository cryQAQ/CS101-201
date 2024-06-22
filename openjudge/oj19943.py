n,m = map(int,input().split())
L,D,A = [[0] * n for _ in range(n)],[[0] * n for _ in range(n)],[[0] * n for _ in range(n)]
for _ in range(m):
    i,j = map(int,input().split())
    D[i][i] += 1
    D[j][j] += 1
    A[i][j],A[j][i] = 1,1
for i in range(n):
    for j in range(n):
        L[i][j] = D[i][j] - A[i][j]
    print(' '.join(map(str,L[i])))