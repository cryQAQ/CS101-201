L = [1,2]
for i in range(2,999999):
    L.append((2 * L[i - 1] + L[i - 2]) % 32767)
n = int(input())
for _ in range(n):
    print(L[int(input()) - 1])