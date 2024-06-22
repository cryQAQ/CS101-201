T,M = map(int,input().split())
L = []
for _ in range(M):
    L.append(list(map(int,input().split())))
dp = [[0] * (T + 1) for _ in range(M + 1)]
for i in range(1,M + 1):
    for j in range(1,T + 1):
        if j >= L[i - 1][0]:
            dp[i][j] = max(dp[i - 1][j],L[i - 1][1] + dp[i - 1][j - L[i - 1][0]])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[M][T])