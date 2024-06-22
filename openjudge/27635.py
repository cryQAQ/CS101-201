visited,flag = set(),False
def dfs(vtx,last):
    global flag,visited
    visited.add(vtx)
    for next in vertices[vtx]:
        if next != last:
            if next in visited:
                flag = True
            else:
                dfs(next,vtx)
    return

n,m = map(int,input().split())
vertices = {}
for i in range(n):
    vertices[i] = []
for _ in range(m):
    a,b = map(int,input().split())
    vertices[a].append(b)
    vertices[b].append(a)
dfs(0,0)
if len(visited) == n:
    print('connected:yes')
else:
    print('connected:no')
if flag:
    print('loop:yes')
else:
    print('loop:no')