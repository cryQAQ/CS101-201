import heapq
n = int(input())
L = list(map(int,input().split()))
heapq.heapify(L)
ans = 0
for _ in range(n - 1):
    x = heapq.heappop(L)
    y = heapq.heappop(L)
    ans += x + y
    heapq.heappush(L,x + y)
print(ans)