t = int(input())
for _ in range(t):
    n = int(input())
    L = list(map(int,input().split()))
    i,j,M,m = 0,n - 1,n,1
    if n >= 3:
        while L[i] == M or L[i] == m or L[j] == M or L[j] == m:
            if L[i] == M:
                i += 1
                M -= 1
            elif L[i] == m:
                i += 1
                m += 1
            if L[j] == M:
                j -= 1
                M -= 1
            elif L[j] == m:
                j -= 1
                m += 1
            if i + 1 == j or i == j:
                break
        if i + 1 == j or i == j:
            print(-1)
        else:
            print(i + 1,j + 1)
    else:
        print(-1)
