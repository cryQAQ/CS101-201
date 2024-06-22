m,n,p=map(int,input().split())
a,way=[],[[0,1],[0,-1],[1,0],[-1,0]]
g={}
for i in range(m):
    a.append([(int(item) if item!='#' else float("inf")) for item in input().split()])
for i in range(m):
    for j in range(n):
        g[(i,j)]=[]
        for k in range(4):
            i2,j2=i+way[k][0],j+way[k][1]
            if a[i][j]!=float("inf") and 0<=i2<m and 0<=j2<n and a[i2][j2]!=float("inf"):
                g[(i,j)].append([(i+way[k][0],j+way[k][1]),abs(a[i][j]-a[i2][j2])])

def dijkstra(xf,yf,ol,cl):
    global g,m,n
    while True:
        if ol=={}:
            return -1
        m=min(ol.values())
        mini_keys=[k for k,v in ol.items() if v==m]
        for key in mini_keys:
            if key==(xf,yf):
                return ol[key]
            cl[key]=ol.pop(key)
        for key in mini_keys:
            for kv in g[key]:
                if kv[0] not in cl:
                    ol[kv[0]]=cl[key]+kv[1] if kv[0] not in ol else min(ol[kv[0]],cl[key]+kv[1])

for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if a[x1][y1]==float("inf") or a[x2][y2]==float("inf"):
        print('NO')
        continue
    ans=dijkstra(x2,y2,{(x1,y1):0},{})
    if ans>=0:
        print(ans)
    else:
        print('NO')