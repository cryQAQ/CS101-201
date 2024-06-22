import math
n = int(input())
N = 0
L = []
L.append(input().split())
a = L[0].count('1')
b = L[0].count('2')
c = L[0].count('3')
d = L[0].count('4')
N += d
if b%2 == 0:
    N += int(b/2)
    if a == c:
        N += a
    elif a < c:
        N += c
    else:
        N += c
        N += math.ceil((a-c)/4)
else:
    N += int((b-1)/2)
    if a == c:
        N += a + 1
    elif a < c:
        N += c + 1
    else:
        N += c
        if a-c <= 2:
            N += 1
        else:
            N += 1 + math.ceil((a-c-2)/4)
print(N)
#compiled by 陈睿阳 2300011406