n = int(input())
l = list(map(int,input().split()))
cnt = 1
for i in range(n):
    l[i]=[max(0,i - l[i]),min(n - 1,i + l[i])]
l.sort(key = lambda x: (x[0],-x[1]))
left,right = l[0][1],l[0][1]
for i in range(1,n):
    right = max(right,l[i][1])
    if l[i][0] >= left + 1:
        left = right
        cnt += 1
print(cnt)