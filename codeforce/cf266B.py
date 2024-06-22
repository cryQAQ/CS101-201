n,t = map(int,input().split())
r = input()
L = []
for i in range(t+1):
    L.append([])
for i in range(len(r)):
    L[0].append(r[i])
for i in range(1,t+1):
    for j in range(len(r)):
        L[i].append(L[i-1][j])
    for j in range(len(r)-1):
        if L[i-1][j] == 'B' and L[i-1][j+1] == 'G':
            L[i][j] = 'G'
            L[i][j+1] = 'B'
ANS = L[t][0]
for i in range(len(r)-1):
    ANS = ANS +L[t][i+1]
print(ANS)