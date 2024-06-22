n = int(input())
while n != 0:
    L = []
    for _ in range(n):
        L.append(list(map(int,input().split())))
    L.sort(key=lambda x :(x[1],x[0]))
    M = L[0][0]
    ans = 1
    for i in range(n):
        if L[i][0] < M:
            ans += 1
            M = L[i][0]
    print(ans)
    n = int(input())