L = set()
n = int(input())
X = []
Y = []
X.append(input().split())
Y.append(input().split())
for i in X[0][1:]:
    i = int(i)
    L.add(i)
for i in Y[0][1:]:
    i = int(i)
    L.add(i)
if len(L) < n:
    print('Oh, my keyboard!')
else:
    print('I become the guy.')
