n,p,m = map(int,input().split())
while not(n == 0 and p == 0 and m == 0):
    L = [True] * n
    ans = []
    cnt = 0
    i,num = p - 1,0
    while cnt < n:
        if L[i % n]:
            num += 1
        if num == m:
            L[i % n] = False
            num = 0
            ans.append(i % n + 1)
            cnt += 1
        i += 1
    print(','.join(map(str,ans)))
    n,p,m = map(int,input().split())