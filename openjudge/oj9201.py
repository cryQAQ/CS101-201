import bisect
N = int(input())
L = list(map(int,input().split()))
l,ans = [],0
for i in L:
    k = bisect.bisect_left(l,i)
    bisect.insort_left(l,i)
    ans += k
print(ans)