n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1,n + 1):
    if i % 2 == 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 2] + dp[i // 2]) % (10 ** 9)
print(dp[-1])