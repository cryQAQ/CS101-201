n = int(input())
s = input()
L = []
for i in range(len(s) // n):
    if i % 2 == 0:
        L.append(list(s[i * n:i * n + n]))
    else:
        L.append(list(s[i * n:i * n + n])[::-1])
ans = str()
for j in range(n):
    for i in range(len(s) // n):
        ans += L[i][j]
print(ans)