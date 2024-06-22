import heapq
n = int(input())
rope = list(map(int,input().split()))
heapq.heapify(rope)
ans = 0
for i in range(n - 1):
    x_1 = heapq.heappop(rope)
    x_2 = heapq.heappop(rope)
    ans += x_1 + x_2
    heapq.heappush(rope,x_1 + x_2)
print(ans)