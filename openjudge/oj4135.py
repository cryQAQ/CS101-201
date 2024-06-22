N,M = map(int,input().split())
L = []
for _ in range(N):
    L.append(int(input()))

def check(dis):
    global L,M,N
    temp,cnt = 0,1
    for i in range(N):
        temp += L[i]
        if temp > dis:
            cnt += 1
            temp = L[i]
    return cnt - M

low = max(L)
high = sum(L) + 1
while low < high:
    mid = (low + high) // 2
    c = check(mid)
    if c > 0:
        low = mid + 1
    else:
        high = mid
print(high)