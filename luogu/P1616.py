t,m = map(int,input().split())
time,value = [],[]
for _ in range(m):
    a,b = map(int,input().split())
    time.append(a)
    value.append(b)
dp = [0] * (t + 1)
for i in range(m):
    for j in range(time[i],t + 1):
        dp[j] = max(dp[j],dp[j - time[i]] + value[i])
print(dp[-1])