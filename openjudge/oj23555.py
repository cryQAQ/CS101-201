n,m_1,m_2 = map(int,input().split())
X,Y,P = [],[],[]
ans = 0
for _ in range(n):
    X.append([0] * n)
    Y.append([0] * n)
    P.append([0] * n)
for _ in range(m_1):
    x,y,i = map(int,input().split())
    X[x][y] = i
for _ in range(m_2):
    x,y,i = map(int,input().split())
    Y[x][y] = i
for i in range(n):
    for j in range(n):
        for k in range(n):
            P[i][j] += X[i][k] * Y[k][j]
for i in range(n):
    for j in range(n):
        if P[i][j] != 0:
            print(i,j,P[i][j])