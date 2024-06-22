from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def is_valid(m,visited,crab):
    return visited[crab[0][0]][crab[0][1]] == 0 and (m[crab[0][0]][crab[0][1]] == 0 or m[crab[0][0]][crab[0][1]] == 5)\
          and (m[crab[1][0]][crab[1][1]] == 0 or m[crab[1][0]][crab[1][1]] == 5)#没来过且不是墙壁
def bfs(m,crab):
    q = deque()
    q.append(crab)
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for i in range(4):
                n_step = [[cur[0][0]+dx[i],cur[0][1]+dy[i]],[cur[1][0]+dx[i],cur[1][1]+dy[i]]]
                if m[n_step[0][0]][n_step[0][1]] == 9 and m[n_step[1][0]][n_step[1][1]] != 1:
                    return True
                elif m[n_step[1][0]][n_step[1][1]] == 9 and m[n_step[0][0]][n_step[0][1]] != 1:
                    return True
                elif is_valid(m,visited,n_step):
                    q.append(n_step)
                    visited[n_step[0][0]][n_step[0][1]] = 1
    return False
n = int(input())
maze = [[1] * (n + 2)]
for _ in range(n):
    maze.append([1] + list(map(int,input().split())) + [1])
maze.append([1] * (n + 2))
crab = []
for i in range(n + 2):
    for j in range(n + 2):
        if maze[i][j] == 5:
            crab.append((i,j))#得到初始值
visited = [[0] * (n + 2) for _  in range(n + 2)]
visited[crab[0][0]][crab[0][1]] = 1
if bfs(maze,crab):
    print('yes')
else:
    print('no')