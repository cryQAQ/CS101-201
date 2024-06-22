n,a,b,c = map(int,input().split())
L = sorted([a,b,c])
f,g = [0] * 4002,[1] + [0] * 4001
g[L[0]],g[L[1]],g[L[2]],g[-1],f[-1] = 1,1,1,0,0
for i in range(L[0],n + 1):
    g[i] = max(g[max(i - L[0],-1)],g[max(i - L[1],-1)],g[max(i - L[2],-1)])
for i in range(1,n + 1):
    f[i] = max(f[max(i - L[0],-1)] + g[max(i - L[0],-1)],f[max(i - L[1],-1)] + g[max(i - L[1],-1)],f[max(i - L[2],-1)] +g[max(i - L[2],-1)])
print(f[n])