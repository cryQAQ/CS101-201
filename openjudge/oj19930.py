from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m,n = map(int,input().split())
maze = []
in_queue = [[False] * n for _ in range(m)]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    in_queue[x][y] = True
    step = 1
    while q:
        for _ in range(len(q)):
            cur_x,cur_y = q.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if 0 <= next_x < m and 0 <= next_y < n and not in_queue[next_x][next_y]:
                    if maze[next_x][next_y] == 1:
                        return step
                    if maze[next_x][next_y] == 0:
                        in_queue[next_x][next_y] = True
                        q.append((next_x,next_y))
        step += 1
    return 'NO'
for _ in range(m):
    maze.append(list(map(int,input().split())))
if maze[0][0] != 1:
    print(bfs(0,0))
else:
    print(0)