n,m = map(int,input().split())
L = list(map(int,input().split()))
distinct = set()
l = 0
cnt = [0] * n
for i in range(n-1,-1,-1):
    if not(L[i] in distinct):
        distinct.add(L[i])
        l += 1
    cnt[i] = l
for _ in range(m):
    i = int(input())
    print(cnt[i - 1])