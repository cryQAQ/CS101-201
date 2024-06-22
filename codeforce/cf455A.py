n = int(input())
num,f = [0] * 100001,[0] * 100001
L = list(map(int,input().split()))
M = max(L)
for i in L:
    num[i] += 1
f[1] = num[1]
for i in range(2,M + 1):
    f[i] = max(f[i - 1],f[i - 2] + num[i] * i)
print(int(f[M]))