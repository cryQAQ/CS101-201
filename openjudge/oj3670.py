L,ans = [],[]
for _ in range(5):
    L.append(list(map(int,input().split())))
for i in range(5):
    M = max(L[i])
    j = L[i].index(M)
    flag = 0
    for k in range(5):
        if M <= L[k][j]:
            flag += 1
    if flag == 5:
        ans.append([i + 1,j + 1,M])
        break
if len(ans) == 0:
    print('not found')
else:
    print(' '.join(map(str,ans[0])))