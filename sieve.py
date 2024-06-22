n = input()
sieve = [True] * (n + 1)
prime = []
for i in range(2,int(n ** 0.5) + 2):
    if sieve[i]:
        for j in range(i,n // i + 1):
            sieve[i * j] = False