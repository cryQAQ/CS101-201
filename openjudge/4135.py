def check(budget,L,num):
    cnt = 1
    cost = 0
    for i in L:
        if cost + i > budget:
            cnt += 1
            cost = i
        else:
            cost += i
    return cnt <= num
N,M = map(int,input().split())
L = []
for _ in range(N):
    L.append(int(input()))
low,high = max(L) - 1,sum(L)
while low < high - 1:
    mid = (low + high) // 2
    if check(mid,L,M):
        high = mid
    else:
        low = mid
print(high)