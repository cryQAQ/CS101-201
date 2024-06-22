n,k = map(int,input().split())
L,ans = [True] * n,[]
left,cnt,i = n,0,0
while left >= 2:
    if L[i % n]:
        cnt += 1
        if cnt == k:
            ans.append(i % n + 1)
            L[i % n] = False
            left -= 1
            cnt = 0
    i += 1
print(' '.join(map(str,ans)))