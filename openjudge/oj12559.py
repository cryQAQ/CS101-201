from functools import cmp_to_key
def pd(a,b):
    l=min(len(a),len(b))
    if a[0:l]>b[0:l]:
        return -1
    if a[0:l]<b[0:l]:
        return 1
    if max(len(a),len(b))==l:
        return 0
    if len(a)>l:
        return pd(a[l:len(a)],b[0:l])
    return pd(a[0:l],b[l:len(b)])
n=int(input())
a=list(map(str,input().split()))
b=sorted(a,key=cmp_to_key(pd))
for i in range(n):
    print(b[i],end='')
print(end=' ')
for i in range(n):
    print(b[n-i-1],end='')