s = input()
r = input()
L = []
for i in range(len(s)):
    L.extend(s[i])
L.reverse()
ans = L[0]
for i in range(1,len(s)):
    ans += L[i]
if ans == r:
    print('YES')
else:
    print('NO')