t = int(input())
for _ in range(t):
    n = int(input())
    L = sorted(list(map(int,input().split())))
    edge = []
    for i in range(n - 1):
        if L[i + 1] != L[i]:
            edge.append((i + 1) * (n - i - 1))
    if len(edge) == 0:
        print(int(n / 2))
    else:
        print(max(edge))