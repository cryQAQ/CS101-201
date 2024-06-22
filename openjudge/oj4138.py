import math
def prime(n):
    a = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,int(math.sqrt(n))+2):
            if n % i == 0:
                a = 0
        return a

S = int(input())
for p in range(int(S / 2) + 1,1,-1):
    if prime(p) != 0 and prime(S-p) != 0:
        print(int(p * (S - p)))
        break