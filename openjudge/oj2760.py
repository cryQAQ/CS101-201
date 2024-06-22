N = int(input())
triangle,dp = [],[]
for _ in range(N):
    triangle.append(list(map(int,input().split())))
    dp.append([-1] * (_ + 1))
for _ in range(N):
    dp[N - 1][_] = triangle[N - 1][_]
for i in range(N - 2,-1,-1):
    for j in range(i + 1):
        dp[i][j] = max(dp[i + 1][j],dp[i + 1][j + 1]) + triangle[i][j]
print(dp[0][0])