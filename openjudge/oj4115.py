from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
m,n,e = map(int,input().split())
maze = [[] for _ in range(m)]
for i in range(m):
    s = input()
    for j in range(n):
        if s[j] == '#':
            maze[i].append(1)
        else:
            maze[i].append(0)
        if s[j] == '@':
            x_s,y_s = i,j
        elif s[j] == '+':
            x_e,y_e = i,j
visited = [[False] * n for _ in range(m)]
visited[x_s][y_s] = e
def is_valid(m,n,cur_x,cur_y,x,y):
    global maze,visited
    return 0 <= x < m and 0 <= y < n and visited[cur_x][cur_y] >= maze[x][y] and not visited[x][y]
def bfs(x_s,y_s,x_e,y_e,m,n):
    global maze,visited
    q = deque()
    q.append((x_s,y_s))
    step = 1
    while q:
        for _ in range(len(q)):
            cur_x,cur_y = q.popleft()
            for i in range(4):
                n_x = cur_x + dx[i]
                n_y = cur_y + dy[i]
                if n_x == x_e and n_y == y_e:
                    return step
                if is_valid(m,n,cur_x,cur_y,n_x,n_y):
                    visited[n_x][n_y] = visited[cur_x][cur_y] - maze[n_x][n_y]
                    q.append((n_x,n_y))
        step += 1
    return -1
print(bfs(x_s,y_s,x_e,y_e,m,n))