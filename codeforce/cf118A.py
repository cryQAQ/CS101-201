s = input()
S = s.lower()
L = []
A = []
for i in range(len(s)):
    L.append(S[i])
for i in range(len(s)):
    n = 0
    for j in['a','e','i','o','u','y']:
        if L[i] != j:
            n += 1
        if n == 6:
            A.append(L[i])
ANS = '.'+'.'.join(A)
print(ANS)
#compiled by 陈睿阳 2300011406