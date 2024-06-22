from math import gcd
a,b,c = map(int,input().split())
G = gcd(gcd(a,b),gcd(b,c))
a,b,c = int(a/G),int(b/G),int(c/G)
num = 0
for i in range(0,int(c/a)+2):
    if int((c - a * i) / b) == (c - a * i) / b and c >= a * i:
        num += 1 
print(num)