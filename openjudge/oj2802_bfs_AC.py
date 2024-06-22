w,h=map(int,input().split())
way=[[1,0],[-1,0],[0,1],[0,-1]]
def bfs(a,p,xf,yf):
    b=[]
    for i in range(h+2):
        b.append([item for item in a[i]])
    b[yf][xf]=0
    while p!=[]:
        x,y,step=p[0][0],p[0][1],p[0][2]
        if x==xf and y==yf :
            return step
        for i in range(4):
            t,dx,dy=1,way[i][0],way[i][1]
            while 0<=x+t*dx<=w+1 and 0<=y+t*dy<=h+1 and b[y+t*dy][x+t*dx]==0:
                b[y+t*dy][x+t*dx]=1
                p.append([x+t*dx,y+t*dy,step+1])
                t+=1
        p.pop(0)
    return -1

l1=1
while w!=0 and h!=0:
    a=[[0]*(w+2)]
    for i in range(1,h+1):
        a.append([0])
        for item in input():
            if item=='X':
                a[i].append(1)
            else:
                a[i].append(0)
        a[i].append(0)
    a.append([0]*(w+2))
    print('Board #'+str(l1)+':')
    x1,y1,x2,y2=map(int,input().split())
    l2=1
    while x1!=0:
        l=bfs(a,[[x1,y1,0]],x2,y2)
        if l>0:
            print('Pair '+str(l2)+':',l,'segments.')
        else:
            print('Pair '+str(l2)+': impossible.')
        x1,y1,x2,y2=map(int,input().split())
        l2+=1
    print()
    w,h=map(int,input().split())
    l1+=1