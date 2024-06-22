ts,te,n = input().split()
h1,m1 = map(int,ts.split(':'))
h2,m2 = map(int,te.split(':'))
T = int((h2 - h1) * 60 + m2 - m1)
n = int(n)
time,value,flag =[],[],[]
for _ in range(n):
    t,c,p = map(int,input().split())
    if p == 0:
        time.append(t)
        value.append(c)
        flag.append(0)
    else:
        cnt = 1
        while p > cnt:
            p -= cnt
            time.append(cnt * t)
            value.append(cnt * c)
            flag.append(1)
        if p > 0:
            time.append(t * p)
            value.append(c * p)
            flag.append(1)
dp = [0] * (T + 1)
for i in range(len(flag)):
    if flag[i] == 0:
        for j in range(time[i],T + 1):
            dp[j] = max(dp[j],dp[j - time[i]] + value[i])
    else:
        for j in range(T,time[i] - 1,-1):
            dp[j] = max(dp[j],dp[j - time[i]] + value[i])
print(dp[-1])