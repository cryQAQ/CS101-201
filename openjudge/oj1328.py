from math import sqrt
cnt = 0
while True:
    n,d = map(int,input().split())
    L = []
    cnt += 1
    if n == 0 and d == 0:
        break
    else:
        flag = 0
        num = 1
        for _ in range(n):
            x,y = map(int,input().split())
            if y <= d:
                L.append([x - sqrt(d ** 2 - y ** 2),x + sqrt(d ** 2 - y ** 2)])
                flag += 1
        if flag == n:
            L.sort(key = lambda x: (x[1],x[0]))
            position = L[0][1]
            for i in range(n):
                if L[i][0] > position:
                    num += 1
                    position = L[i][1]
            print('Case',str(cnt)+':',str(num))
        else:
            print('Case',str(cnt)+':',str(-1))
    s = input()