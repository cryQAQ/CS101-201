N = int(input())
for i in range(N):
    n,k = map(int,input().split())
    s = input()
    R = []
    a = 0
    b = 0
    for i in range(n):
        R.append(ord(s[i]))
    for i in range(n):
        for j in range(n):
            if R[i] == R[j] + 32 or R[i] == R[j] - 32:
                a += 1
            if R[i] == R[j]:
                b += 1