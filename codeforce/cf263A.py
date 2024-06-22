for i in range(5):
    a,b,c,d,e=map(int,input().split())
    if a == 1:
        ans = 2+abs(2-i)
    elif b == 1:
        ans = 1+abs(2-i)
    elif c == 1:
        ans = abs(2-i)
    elif d == 1:
        ans = 1+abs(2-i)
    elif e == 1:
        ans = 2+abs(2-i)
print(ans)
#compiled by 陈睿阳 2300011406