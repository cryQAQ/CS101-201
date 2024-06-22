step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
M = []
for _ in range(10):
    M.append(list(input()))

def check(x,y):
    return 0 <= x < 10 and 0 <= y < 10 and M[x][y] == '.'

def dfs(cur_pt):
    x, y = cur_pt
    M[x][y] = '-'
    for choice in step:
        next_x, next_y = x + choice[0], y + choice[1]
        if check(next_x, next_y):
            dfs((next_x, next_y))
    return

def search(M):
    cnt = 0
    for i in range(10):
        for j in range(10):
            if check(i,j):
                cnt += 1
                dfs((i, j))
    return cnt

print(search(M))