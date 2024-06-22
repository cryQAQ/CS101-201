n = int(input())
dp = [['()']]
for t in range(1,n):
    raw = []
    for p in dp[t - 1]:
        for i in range(2 * t - 1):
            if p[i] == ')':
                raw.append(p[:i + 1]+'()'+p[i + 1:])
            else:
                cnt = 0
                for j in range(i,2 * t):
                    if p[j] == '(':
                        cnt += 1
                    else:
                        cnt -= 1
                    if cnt == 0:
                        raw.append(p[:i] + '('+p[i:j] + ')' + p[j:])
        raw.append(p+'()')
    dp.append(list(set(raw)))
print(dp[-1])