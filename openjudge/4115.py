import queue
step = [(-1,0),(1,0),(0,1),(0,-1)]
M,N,T = map(int,input().split())
def check(i,j):
    return 0 <= i < M and 0 <= j < N
graph = []
for _ in range(M):
    graph.append(list(input()))
for i in range(M):
    for j in range(N):
        if graph[i][j] == '@':
            s_i,s_j = i,j

def bfs():
    q = queue.Queue()
    q.put((s_i,s_j,T,0))
    while not q.empty():
        i,j,e,d = q.get()
        if graph[i][j] == '+':
            return d
        for s in step:
            next_i,next_j = i + s[0],j + s[1]
            if check(next_i,next_j):
                if graph[next_i][next_j] == '*':
                    q.put((next_i,next_j,e,d + 1))
                elif graph[next_i][next_j] == '#':
                    if e >= 1:
                        q.put((next_i,next_j,e - 1,d + 1))
    return -1
print(bfs())