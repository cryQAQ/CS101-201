import math
N,A,B = map(int,input().split())
z = []
m = []
for i in range(1,N+1):
    for j in range(1,i):
        if j/i<A/B and math.gcd(i,j) == 1:
            z.append(j)
            m.append(i)
ans1 = z[0]
ans2 = m[0]
for i in range(1,len(z)):
    if float(z[i]/m[i]) > float(ans1/ans2):
        ans1 = z[i]
        ans2 = m[i]
print(str(ans1),str(ans2))
