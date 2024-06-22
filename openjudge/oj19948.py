n,m= map(int,input().split())
L = sorted(list(map(int,input().split())))
gap = []
for i in range(n - 1):
    gap.append(L[i + 1] - L[i])
gap.sort()
print(sum(gap[:n - m ]))