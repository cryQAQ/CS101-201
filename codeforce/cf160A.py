n = int(input())
L = list(map(int,input().split()))
L.sort()
L.reverse()
i = 1
while sum(L[:i]) <= sum(L) - sum(L[:i]):
    i += 1
print(i)
#compiled by 陈睿阳 2300011406
