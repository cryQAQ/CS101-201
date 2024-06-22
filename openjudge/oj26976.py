n = int(input())
l = list(map(int,input().split()))
num = 0
L = [l[0]]
for i in range(1,n):
    if l[i] != L[-1]:
        L.append(l[i])
if len(L) == 1:
    print(1)
else:
    for i in range(1,len(L) - 1):
        if L[i] > L[i - 1] and L[i] > L[i + 1]:
            num += 1
        elif L[i] < L[i - 1] and L[i] < L[i + 1]:
            num += 1
    print(num + 2)