n,m = map(int,input().split())
L = [[0] * (m + 2)]
NEW = []
for _ in range(n):
    L.append([0] + list(map(int,input().split())) + [0])
L.append([0] * (m + 2))
for _ in range(n):
     NEW.append([0] * m)
for i in range(1,n + 1):
    for j in range(1,m + 1):
            S = L[i - 1][j - 1] + L[i][j - 1] + L[i + 1][j - 1] + L[i - 1][j] + L[i + 1][j] + L[i - 1][j + 1] + L[i][j + 1] + L[i + 1][j + 1]
            if L[i][j] == 1:
                 if S == 2 or S == 3:
                    NEW[i - 1][j - 1] = 1
            else:
                 if S == 3:
                    NEW[i - 1][j - 1] = 1
for i in range(n):
    print(' '.join(map(str,NEW[i])))