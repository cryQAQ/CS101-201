C = int(input()) 
for _ in range(C):
    total = 0
    n,m,b = map(int,input().split())
    T = set()
    D = {}
    for i in range(n):
        time,damage = map(int,input().split())
        if not(time in T):
            T.add(time)
            D[time] = [damage]
        else:
                D[time].append(damage)
    C = sorted(D)
    for key in C:
        if m >= len(D[key]):
            total += sum(D[key])
        else:
            D[key] = sorted(D[key],reverse=True)
            total += sum(D[key][:m])
        if total >= b:
             print(key)
             break
    if total < b:
         print('alive')