n = int(input())
L = list(map(int,input().split()))
l = []
order = []
for i in range(n):
    l.append([i,L[i]])
l.sort(key=lambda x: x[1])
for i in l:
    order.append(i[0] + 1)
print(' '.join(map(str,order)))
time = 0
for i in range(n):
    time += l[i][1] * (n - 1 -i)
print('{:.2f}'.format(time / n))