t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    L = list(map(int,input().split()))
    if sum(L) % x != 0:
        print(n)
    else:
        i = 0
        j = -1
        while i < n and L[i] % x == 0:
            i += 1
        while j > - n and L[j] % x == 0:
            j -= 1
        if i == n or j == -n:
            print(-1)
        else:
            print(n-min([i,- j - 1])-1)
#compiled by 陈睿阳 2300011406