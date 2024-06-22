k,n,w = map(float,input().split())
ans = w*(w+1)/2*k - n
ans = int(ans)
if ans > 0:
    print(ans)
else:
    print(0)
