n = int(input())
x,h = [],[]
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    h.append(b)
end,cnt = x[0],2
for i in range(1,n - 1):
    if x[i] - end > h[i]:
        cnt += 1
        end = x[i]
    elif x[i + 1] - x[i] > h[i]:
        cnt += 1
        end = x[i] + h[i]
    else:
        end = x[i]
if n != 1:
    print(cnt)
else:
    print('1')