t = int(input())
time = []
for _ in range(t):
    A = set()
    table = {}
    F = []
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        if a[i] in A:
            table[a[i]] += b[i]
        else:
            A.add(a[i])
            table[a[i]] = b[i]
    a = sorted(list(A),reverse=True)
    fetch,i = 0,0
    if a[-1] >= sum(b):
        ans = sum(b)
    elif a[0] < table[a[0]]:
        ans = a[0]
    else:
        for i in range(len(a)):
            fetch += table[a[i]]
            F.append(fetch)
        i = 0
        while a[i] >= F[i]:   
            i += 1
        ans = max(F[i - 1],a[i])
    time.append(ans)
for ans in time:
    print(ans)