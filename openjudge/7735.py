import heapq
K = int(input())
N = int(input())
R = int(input())
graph = {i:{} for i in range(1,N + 1)}
for _ in range(R):
    S,D,L,T = map(int,input().split())
    graph[S][D] = (L,T)
def dijk():
    q = []
    heapq.heappush(q,(0,1,K))
    while q:
        distance,city,money = heapq.heappop(q)
        if city == N:
            return distance
        for next_city in graph[city]:
            new_dis,cost = graph[city][next_city]
            if money >= cost:
                heapq.heappush(q,(distance + new_dis,next_city,money - cost))
    return -1
print(dijk())