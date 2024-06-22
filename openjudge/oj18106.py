n = int(input())
L = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        circ = min(i,j, n - 1 - i,n - 1 - j)
        if circ > 0:
            N = 4 * (n - circ) * circ
        else:
            N = 0
        if i == circ:
            L[i][j] = N + j - circ + 1
        elif j == circ:
            L[i][j] = N + 4 * (n - 2 * circ - 1) - i + circ + 1
        elif i == n - circ - 1:
            L[i][j] = N + 2 * (n - 2 * circ) - 1 + n - circ - 1 - j
        elif j == n - circ - 1:
            L[i][j] = N + n - 2 * circ + i - circ 
for i in range(n):
    print(' '.join(map(str,L[i])))