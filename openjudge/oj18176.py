from math import sqrt
prime = [1] * (10001)
for i in range(2,101):
    if prime[i] == 1:
        for j in range(i,10000 // i + 1):
            prime[i * j] = 0  
m,n = map(int,input().split())
for _ in range(m):
    grade = list(map(int,input().split()))
    total = 0
    for i in range(len(grade)):
        sq = sqrt(grade[i])
        if int(sq) == sq:
            sq = int(sq)
            total += grade[i] * prime[sq]    
    print("{:.2f}".format(total/len(grade)))