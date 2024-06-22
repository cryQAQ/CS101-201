import heapq
T = int(input())
for _ in range(T):
    l = list(map(int,input().split()))
    if len(l) % 2 == 0:
        l = l[:-1]
    ans = []
    L = [l[0]]
    heapq.heapify(L)
    for i in range(1,len(l)):
        heapq.heappush(L,l[i])
        if i % 2 == 0:
            ans.append(L[i // 2])
    print(len(ans))
    print(' '.join(map(str,ans)))