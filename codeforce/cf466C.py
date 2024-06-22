n = int(input())
array = list(map(int,input().split()))
L,s,num,S = [],sum(array),0,0
if s != 0:
    for i in range(n):
        S += array[i]
        if S == s / 3:
            L.append(1)
        elif S == 2 * s / 3:
            L.append(2)
        else:
            L.append(0)
    cnt = L.count(2)
    for i in range(n):
        if L[i] == 1:
            num += cnt
        elif L[i] == 2:
            cnt -= 1
else:
    cnt = 0
    for i in range(n):
        S += array[i]
        if S == 0:
            cnt += 1
    num = int((cnt - 1) * (cnt - 2) / 2)
print(num)