def join(x,y):
    fx,fy=find(x),find(y)
    if fx!=fy:
        if h[fx]<h[fy]:
            a[fx]=fy
        else:
            a[fy]=fx
            if h[fx]==h[fy]:
                h[fx]+=1
def find(x):
    if a[x]!=x:
        a[x]=find(a[x])
    return a[x]

n,k=map(int,input().split())
s=0
a=[i for i in range(3*n)]
h=[0]*(3*n)
for _ in range(k):
    d,x,y=map(int,input().split())
    if x>n or y>n:
        s+=1
        continue
    if x==y:
        if d==2:
            s+=1
        continue
    x,y=x-1,y-1
    if d==1:
        if find(x)==find(y+n) or find(y)==find(x+n):
            s+=1
            continue
        join(x,y),join(x+n,y+n),join(x+2*n,y+2*n)
    if d==2:
        if find(x)==find(y) or find(x)==find(y+n):
            s+=1
            continue
        join(x+n,y)
        join(x+2*n,y+n)
        join(x,y+2*n)
print(s)