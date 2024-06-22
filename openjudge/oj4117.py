while True:
    try:
        n = int(input())
        dp = [[0] * n for _ in range(n)]#dp[i][j]表示使用不超过j的数字组成i的可能情况数
        for i in range(n):
            dp[i][0] = 1
            dp[0][i] = 1
        for i in range(1,n):
            for j in range(1,i):
                dp[i][j] = dp[i][j - 1] + dp[i - j - 1][j]
            dp[i][i] = dp[i][i - 1] + 1
            for j in range(i + 1,n):
                dp[i][j] = dp[i][i]
        print(dp[-1][-1])
    except EOFError:
        break