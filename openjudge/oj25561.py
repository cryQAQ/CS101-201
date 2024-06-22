N,m=map(int,input().split());A=[];B=[0];C=[0];D=[]
for _ in range(N):A+=[[*map(lambda x:[*map(int,x.split(":"))],input().split())]]
for _ in range(m):B+=[[*map(lambda x:[*map(int,x.split("-"))],input().split())]]
def f(t,P):
    global C
    if t==N:C+=[[sum(P)]+P[1:]];return
    for i in A[t]:P[i[0]]+=i[1];f(t+1,P);P[i[0]]-=i[1]
f(0,[0]*(m+1));del C[0]
for K in C:
    t=K[0]-K[0]//300*50
    for i in range(1,m+1):t-=max([x[1]for x in B[i] if x[0]<=K[i]]+[0])
    D+=[t]
print(min(D))