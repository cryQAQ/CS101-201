def sol(graph,n,k,visited):
    if len(graph) == 1:
        if k == 1:
            ans = 0
            for i in range(n):
                if graph[0][i] == '#' and not i in visited:
                    ans += 1
            return ans 
        if k == 0:
            return 1
        if k > 1:
            return 0
    ans = sol(graph[1:],n,k,visited)
    for i in range(n):
        if graph[0][i] == '#' and not i in visited:
            visited.append(i)
            ans += sol(graph[1:],n,k - 1,visited)
            visited.pop()
    return ans

n,k = map(int,input().split())
while n != -1 and k != -1:
    G = []
    for _ in range(n):
        G.append(list(input()))
    print(sol(G,n,k,[]))
    n,k = map(int,input().split())