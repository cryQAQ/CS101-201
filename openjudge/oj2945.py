n = int(input())
L = list(map(int,input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if L[j] >= L[i]:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))
#其实这个dp构造还是蛮巧妙的，类似LIS