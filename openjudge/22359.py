sieve = [True] * (10001)
for i in range(2,102):
    if sieve[i]:
        for j in range(i,10000 // i + 1):
            sieve[i * j] = False
S = int(input())
i = 2
while i <= S // 2:
    if sieve[i] and sieve[S - i]:
        print(i,S-i)
        break
    i += 1