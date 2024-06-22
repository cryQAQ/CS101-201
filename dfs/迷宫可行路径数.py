dx = [-1,0,0,1]
dy = [0,-1,1,0]
def dfs(m,x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if m[nx][ny] == 'e':
            cnt += 1
            continue
        elif m[nx][ny] == 0:
            m[x][y] = 1
            dfs(m,nx,ny)
            m[x][y] = 0
    return
n,m = map(int,input().split())
cnt = 0
M = [[-1] * (m + 2)]
for _ in range(n):
    M.append([-1] + list(map(int,input().split())) + [-1])
M.append([-1] * (m + 2))
M[1][1] = 's'
M[n][m] = 'e'
dfs(M,1,1)
print(cnt)