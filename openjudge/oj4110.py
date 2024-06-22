n,w = map(int,input().split())
L = []
ans = 0
for _ in range(n):  
    a,b = map(int,input().split())
    L.append([a,b,a / b])
func = lambda x:x[2]
L = sorted(L,key = func,reverse=True)
i = 0
S = L[0][1]
s = 0
for _ in range(len(L)):
    s += L[_][1]
if  s > w:
    while S <= w:
        i += 1
        S += L[i][1]
    S -= L[i][1]
    for j in range(i):
        ans += L[j][0]
    ans += (w - S) * L[i][2]
    print("{:.1f}".format(ans))
else:
    ans = 0
    for _ in range(len(L)):
        ans += L[_][0]
    print("{:.1f}".format(ans))