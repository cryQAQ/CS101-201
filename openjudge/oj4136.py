R = int(input())
N = int(input())
l = [0] * R
for _ in range(N):
    L,T,W,H = map(int,input().split())
    for i in range(L,L + W):
        l[i] += H
left,right = 0,R - 1
S = sum(l)
while left < right:
    mid = (left + right) // 2
    s = sum(l[:mid])
    if s > S - s:
        left = mid
    else:
        right = mid - 1
print(left)