flag = False
visited = set()
def dfs(vtx):
    global flag, visited
    if not flag:
        for next_vtx in D[vtx]:
            if next_vtx in visited:
                flag = True
                return
            if not edge[(vtx,next_vtx)]:
                visited.add(next_vtx)
                edge[(vtx,next_vtx)] = True
                dfs(next_vtx)
                visited.remove(next_vtx)
        return
    return
        
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    D = {}
    edge = {}
    for i in range(N):
        D[i + 1] = []
    for _ in range(M):
        x,y = map(int,input().split())
        edge[(x,y)] = False
        D[x].append(y)
    flag = False
    for i in range(1,N + 1):
        visited = set()
        dfs(i)
    print('Yes' if flag else 'No')