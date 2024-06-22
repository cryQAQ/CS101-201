n,m = map(int,input().split())
dp = [([1] + [0] * (m - 1)) for _ in range(n + 1)]
dp[0] = [1] * m
for i in range(1,n + 1):
    for j in range(1,m):
        if i >= j:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = 2 ** i
print(dp[n][m - 1])