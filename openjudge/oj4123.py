d = [(-2,-1),(-1,-2),(2,-1),(-1,2),
       (-2,1),(1,-2),(2,1),(1,2)]
num = 0
def is_valid(maze,m,n,x,y):
    return 0 <= x < n and 0 <= y < m and not maze[x][y]
def dfs(maze,m,n,x,y,step):
    if step == m * n:
        global num
        num += 1
        return
    maze[x][y] = True
    for i in range(8):
        next_x = x + d[i][0]
        next_y = y + d[i][1]
        if is_valid(maze,m,n,next_x,next_y):
            dfs(maze,m,n,next_x,next_y,step + 1)
    maze[x][y] = False
T = int(input())
for i in range(T):
    n,m,x,y = map(int,input().split())
    num = 0
    maze = [[False] * m for _ in range(n)]
    maze[x][y] = True
    dfs(maze,m,n,x,y,1)
    print(num)