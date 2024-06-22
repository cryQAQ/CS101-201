L = [0,1,1]
n = int(input())
if n <= 2:
    print(L[n])
else:
    for _ in range(n - 2):
        L.append(L[-1] + L[-2] + L[-3])
    print(L[-1])