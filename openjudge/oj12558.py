n,m = map(int,input().split())
M,num,ans = [[0] * (m + 2)],0,0
for _ in range(n):
    R = list(map(int,input().split()))
    M.append([0] + R + [0])
M.append([0] * (m + 2))
for i in range(n + 2):
    for j in range(m + 2):
        if M[i][j] == 1:
            num += M[i - 1][j] + M[i][j - 1] + M[i][j + 1] + M[i + 1][j]
            ans += 4
print(ans - num)    