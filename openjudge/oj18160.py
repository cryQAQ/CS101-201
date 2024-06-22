dire = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def dfs(x,y):
    num = 1
    m[x][y] = '.'
    for i in range(8):
        if m[x + dire[i][0]][y + dire[i][1]] == 'W':
            num += dfs(x + dire[i][0],y + dire[i][1])
    return num
T = int(input())
for _ in range(T):
    ans = []
    N,M = map(int,input().split())
    m = [['.'] * (M + 2)]
    for i in range(N):
        m.append(['.'] + list(input()) + ['.'])
    m.append(['.'] * (M + 2))
    for i in range(1,N + 1):
        for j in range(1,M + 1):
            if m[i][j] == 'W':
                ans.append(dfs(i,j))
    if len(ans) == 0:
        print(0)
    else:
        print(max(ans))