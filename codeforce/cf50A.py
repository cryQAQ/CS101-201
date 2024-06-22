m,n = map(int,input().split())
if m%2 == 0 or n%2 == 0:
    print(int(m*n/2))
else:
    print(int((m*n-1)/2))