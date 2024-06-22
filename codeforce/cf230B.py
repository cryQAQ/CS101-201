from math import sqrt
prime = []
n_prime = [1] * 2 + [0] * 999999
for i in range(2, 1000001):
    if not n_prime[i]:
        prime.append(i)
    for p in prime:
        if i * p > 1000000:
            break
        n_prime[i * p] = 1
        if i % p == 0:
            break

n = int(input())
num = input().split()
for i in range(n):
    num[i] = int(num[i])
    if int(sqrt(num[i])) != sqrt(num[i]):
        print('NO')
    else:
        if not n_prime[int(sqrt(num[i]))]:  
            print('YES')
        else:
            print('NO')