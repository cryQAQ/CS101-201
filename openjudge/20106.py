import queue
m,n,p = map(int,input().split())
M = []
step = [(0,-1),(0,1),(1,0),(-1,0)]
for _ in range(m):
    M.append(list(input().split()))
for i in range(m):
    for j in range(n):
        if M[i][j] != '#':
            M[i][j] = int(M[i][j])
def check(i,j):
    return 0 <= i < m and 0 <= j < n and M[i][j] != '#'
def bfs(s_i,s_j,e_i,e_j):
    dis = [[float('inf')] * n for _ in range(m)]
    q = queue.Queue()
    q.put((s_i,s_j))
    dis[s_i][s_j] = 0
    while not q.empty():
        x,y = q.get()
        for s in step:
            n_x,n_y = x + s[0],y + s[1]
            if check(n_x,n_y):
                if dis[n_x][n_y] > dis[x][y] + abs(M[n_x][n_y] - M[x][y]):
                    dis[n_x][n_y] = dis[x][y] + abs(M[n_x][n_y] - M[x][y])
                    q.put((n_x,n_y))
    if dis[e_i][e_j] != float('inf'):
        return dis[e_i][e_j]
    return 'NO'
for _ in range(p):
    s_i,s_j,e_i,e_j = map(int,input().split())
    if M[s_i][s_j] == '#' or M[e_i][e_j] == '#':
        print('NO')
    else:
        print(bfs(s_i,s_j,e_i,e_j))