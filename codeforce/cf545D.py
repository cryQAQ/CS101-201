n = int(input())
L = sorted(list(map(int,input().split())))
N = [L[0]]
start = 0
if n > 1:
    while L[-1] >= sum(N):
        for i in range(start + 1,n):
            if L[i] >= sum(N):
                start = i
                N.append(L[i])
                break
    print(len(N))
else:
    print(1)