n,t = map(int,input().split())
p = list(map(int,input().split()))
if sum(p)<t:
    print(0)
else:
    dp = [0] + [float('inf')] * t
    for i in range(n):
        now = p[i]
        if now > t:
            for x in range(1,t + 1):
                dp[x] = min(dp[x], now)
        else:
            for c in range(t, now - 1, -1):
                dp[c] = min(dp[c], now + dp[c - now])
            for d in range(now - 1, -1, -1):
                dp[d] = min(dp[d], now)
    print(dp[-1])