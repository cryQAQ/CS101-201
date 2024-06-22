n = int(input())
X = 0
Y = 0
Z = 0
for i in range(n):
    a,b,c =  map(int,input().split())
    X += a
    Y += b
    Z += c
if X == 0 and Y == 0 and Z == 0:
    print("YES")
else:
    print("NO")
#compiled by 陈睿阳 2300011406