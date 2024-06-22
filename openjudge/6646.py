n = int(input())
L = [1] * (n + 1)
for i in range(n):
    for j in map(int,input().split()):
        if j != -1:
            L[j] = L[i + 1]+1
print(max(L))