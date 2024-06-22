from itertools import product
from copy import deepcopy
light,operation = [],[[] for _ in range(64)]
dx = [0,0,0,-1,1]
dy = [-1,1,0,0,0]
def switch(m,x,y):
    for i in range(5):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0 <= n_x < 5 and 0 <= n_y < 6:
            if m[n_x][n_y] == 0:
                m[n_x][n_y] = 1
            else:
                m[n_x][n_y] = 0
    return
a,cnt = [0,1],0
for _ in product(a,repeat=6):
    operation[cnt].append(list(_))
    for __ in range(4):
        operation[cnt].append([0] * 6)
    cnt += 1
for _ in range(5):
    light.append(list(map(int,input().split())))
for i in range(64):
    copy = deepcopy(light)
    for j in range(6):
        if operation[i][0][j] == 1:
            switch(copy,0,j)
    for j in range(1,5):
        for k in range(6):
            if copy[j - 1][k] == 1:
                switch(copy,j,k)
                operation[i][j][k] = 1
    if sum(copy[4]) == 0:
        for j in range(5):
            print(' '.join(map(str,(operation[i][j]))))
        break