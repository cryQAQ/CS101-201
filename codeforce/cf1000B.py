n,M = map(int,input().split())
a = [0] + list(map(int,input().split())) + [M]
L,t = [],0
delta = 0
for i in range(1,n + 1):
    if i % 2 == 1:
        t += a[i] - a[i - 1]
    L.append(t)
if n % 2 == 0:
    t += M - a[-2]
for i in range(n):
    L[i] = t - L[i]
for i in range(1,n + 1):
    if not(a[i] - 1 == a[i - 1] and a[i] + 1 == a[i + 1]):
        if delta < M - a[i] - 2 * L[i - 1] - 1:
            delta = M - a[i] - 2 * L[i - 1] - 1
print(t + delta)