from collections import defaultdict
def add(a):
    i=0
    while 1:
        m,n=a[i],a[i+1]
        if n<0:
            break
        res[n]+=m
        i+=2
for _ in range(int(input())):
    res=defaultdict(int)
    add(list(map(int,input().split())))
    add(list(map(int,input().split())))
    for i in sorted(res,reverse=True):
        if res[i]!=0:
            print(f'[ {res[i]} {i} ] ',end='')
    print()