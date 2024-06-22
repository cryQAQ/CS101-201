from math import sqrt
prime = 2
table = [True] * 2 + [False] * (1999)
while prime <= sqrt(2000):
    for i in range(2,int(2000 / prime) + 1):
        table[prime * i] = True
    for i in range(prime + 1,2001):
        if table[i] == False:
            prime = i
            break
n = int(input())
if n < 6 or n % 2 != 0:
    print("Error!")
else:
    for i in range(2,int(n / 2) + 1):
        if table[i] == False and table[n - i] == False:
            print(str(n)+'='+str(i)+'+'+str(n - i))