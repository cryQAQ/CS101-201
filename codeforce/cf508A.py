n,m,k = map(int,input().split())
screen = []
flag = 0
F = 0
for _ in range(n+2):
    screen.append([0] * (m + 2))
for _ in range(k):
    x,y = map(int,input().split())
    screen[x][y] = 1
    for i in range(x - 1,x + 1):
        if F == 0:
            for j in range(y - 1,y + 1):
                if screen[i][j]&screen[i + 1][j]&screen[i][j + 1]&screen[i + 1][j + 1] == 1:
                    print(_ + 1)
                    F = 1
                    break
                else:
                    flag += 1
        else:
            break
if flag == k * 4:
    print('0')