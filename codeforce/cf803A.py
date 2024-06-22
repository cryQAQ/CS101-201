n,k = map(int,input().split())
M = [[0] * n for _ in range(n)]
i = j = 0
if k <= n ** 2:
    while k > 1:
        if i == j:
            M[i][i] = 1
            k -= 1
        elif j > i:
            M[i][j],M[j][i] = 1,1
            k -= 2
        j += 1
        if j == n:
            i += 1
            j = 0
    if k == 1:
        if j == 0:
            M[i][i] = 1
        else:
            M[i + 1][i + 1] = 1
    for i in range(n):
        print(' '.join(map(str,M[i])))
else:
    print(-1)