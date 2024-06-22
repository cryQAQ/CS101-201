import math
def f(num):
    factors = []
    sq = int(math.sqrt(num))
    for i in range(1,sq+1):
        if num%i == 0:
            factors.append(i)
            factors.append(int(num/i))
    factors.sort()
    return(factors)
n = int(input())
for i in range(n):
    x = int(input())
    L = []
    for j in range(len(f(x))-1):
            if f(x)[i+1] == f(x)[i] + 1:
                L.append(1)
            else:
                L.append(0)
    S = []
    for j in range(len(L)):
         if L[j] == 1:
              S.append(L[j]+1)
    S.sort()
    print(S[-1])
#没搞懂
