from collections import deque
n = int(input())
maze = []
step = [(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(n):
    maze.append(list(map(int,list(input()))))
visited = [[False] * n for _ in range(n)]
q = deque()
def check(x,y):
    global maze,visited
    return 0 <= x < n and 0 <= y < n and not visited[x][y]
def dfs(x,y):#标记同一个岛屿，并且确定所有岸边起点
    global maze,visited,step,q
    visited[x][y] = True
    cnt = 0
    for i in range(4):
        n_x,n_y = x + step[i][0],y + step[i][1]
        if 0 <= n_x < n and 0 <= n_y < n and maze[n_x][n_y] == 1:
            cnt += 1
        elif x < 0 or x >= n or y < 0 or y >= n:
            cnt += 1
    if cnt < 4:
        q.append((x,y))
    for i in range(4):
        n_x,n_y = x + step[i][0],y + step[i][1]
        if check(n_x,n_y) and maze[n_x][n_y] == 1:
            dfs(n_x,n_y)
            return
def search(maze,n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 1:
                return i,j
x1,y1 = search(maze,n)       
dfs(x1,y1)
ans,flag = 0,False
while q:
    if not flag:
        for _ in range(len(q)):
            x,y = q.popleft()
            if maze[x][y] == 1 and not visited[x][y]:
                print(ans - 1)
                flag = True
                break
            for i in range(4):
                n_x,n_y = x + step[i][0],y + step[i][1]
                if check(n_x,n_y):
                    q.append((n_x,n_y))
        ans += 1
    else:
        break