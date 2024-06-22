L = list(map(int,input().split()))
cnt = [0] * (max(L) + 1)
for i in L:
    cnt[i] += 1
ans,m = [],0
for i in range(len(cnt)):
    if cnt[i] > m:
        m = cnt[i]
        ans = [i]
    elif cnt[i] == m:
        ans.append(i)
print(' '.join(map(str,ans)))