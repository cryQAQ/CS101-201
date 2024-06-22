from heapq import heappop,heappush
from copy import deepcopy
direction = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(i,j):
    visited = set();q =  [(0,i,j)]
    while q:
        energy,x,y = heappop(q)
        visited.add((x,y))
        if x == x_2 and y == y_2:
            return energy
        for k in range(4):
            dx,dy = direction[k]
            n_x,n_y = x + dx,y + dy
            if 0 <= n_x < m and 0 <= n_y < n and cur[n_x][n_y] != '#' and not (n_x,n_y) in visited:
                heappush(q,(energy + abs(cur[n_x][n_y] - cur[x][y]),n_x,n_y))
    return -1
m,n,p = map(int,input().split())
maze = []
for _ in range(m):
    maze.append([])
    for i in input().split():
        if i != '#':
            maze[-1].append(int(i))
        else:
            maze[-1].append(i)
for _ in range(p):
    x_1,y_1,x_2,y_2 = map(int,input().split())
    cur = deepcopy(maze)
    if maze[x_1][y_1] == '#' or maze[x_2][y_2] == '#':
        print('NO')
    else:
        ans = bfs(x_1,y_1)
        if ans == -1:
            print('NO')
        else:
            print(ans)