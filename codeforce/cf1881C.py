t = int(input())
for _ in range(t):
    n = int(input())
    L = []
    cnt = 0
    for i in range(n):
        L.append(list(input()))
    for i in range(n // 2):
        for j in range(i,n - i - 1):
            num = sorted([ord(L[i][j]),ord(L[j][n - i - 1]),ord(L[n - i - 1][n - j - 1]),ord(L[n - j - 1][i])])
            cnt += 3 * num[3] - num[2] - num[1] - num[0]
    print(cnt)