from collections import deque
m,n = map(int,input().split())
ans = 0
L = list(map(int,input().split()))
RAM,l = deque(),0
for i in range(n):
    if (not L[i] in RAM) and l < m:
        l += 1
        RAM.append(L[i])
        ans += 1
    elif (not L[i] in RAM) and l == m:
        RAM.popleft()
        RAM.append(L[i])
        ans += 1
print(ans)