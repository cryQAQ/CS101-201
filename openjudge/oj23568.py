n = int(input())
plan = []
for _ in range(n):
    s,e,score = input().split()
    if s[0] == '1':
        s = int(s[2:]) - 7
    else:
        s = int(s[2:]) + 24
    if e[0] == '1':
        e = int(e[2:]) - 7
    else:
        e = int(e[2:]) + 24
    if e <= 44:
        plan.append((s,e,int(score)))
plan.sort(key=lambda x :x[1])
dp = [0] * 46
for p in plan:
    for j in range(p[1] + 1,46):
        dp[j] = max(dp[j],dp[p[0]] + p[2])
print(dp[-1])