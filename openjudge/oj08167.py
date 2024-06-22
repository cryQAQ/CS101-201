n,m = map(int,input().split())
L = []
for _ in range(n):
    row = list(map(int,input().split()))
    L.append(row)
firstrow = []
lastrow = []
for i in range(m):
    firstrow.append(str(L[0][i]))
    lastrow.append(str(L[-1][i]))
print(' '.join(firstrow))
newrow = []
for i in range(1,n-1):
    newrow.append(str(L[i][0]))
    for j in range(1,m-1):
        average = (L[i-1][j]+L[i][j-1]+L[i][j]+L[i][j+1]+L[i+1][j])//5
        newrow.append(str(average))
    if m!= 1:
        newrow.append(str(L[i][-1]))
    print(' '.join(newrow))
    newrow.clear()
if n != 1:
    print(' '.join(lastrow))