#dfs,TLE
dx = [0,0,1,-1]
dy = [1,-1,0,0]
w,h = map(int,input().split())
cnt_board = 1
step,min_step,flag = 0,0,False
def is_valid(x,y):
    return 0 <= x < h + 2 and 0 <= y < w + 2 and not visited[x][y] and maze[x][y] == ' '
def dfs(x,y,x_2,y_2):
    global cur_path,step,min_step,flag
    if x == x_2 and y == y_2:
        if flag:
            if step < min_step:#更新最小值
                min_step = step
        else:
            min_step = step
            flag = True
        return 
    if step < min_step or not flag:#剪枝，如果已经比最小值大了，则不用继续
        visited[x][y] = True
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if is_valid(next_x,next_y) or next_x == x_2 and next_y == y_2:#下一个可走或者到达目标
                cur_path.append([next_x,next_y])
                if x != x_1 or y != y_1:
                    if abs(next_x - cur_path[-3][0]) != 2 and abs(next_y - cur_path[-3][1]) != 2:#判断转弯
                        step += 1
                dfs(next_x,next_y,x_2,y_2)#递归
                next_x = x + dx[i]
                next_y = y + dy[i]
                if x != x_1 or y != y_1:
                    if abs(next_x - cur_path[-3][0]) != 2 and abs(next_y - cur_path[-3][1]) != 2:#判断转弯
                        step -= 1
                cur_path.pop()
        visited[x][y] = False#回溯
    else:
        return
while w != 0 and h != 0:
    print('Board #'+str(cnt_board)+':')
    cnt_board += 1
    cnt_pair = 1
    maze = [' ' * (w + 2)]
    for i in range(h):
        maze.append(' '+input()+' ')
    maze.append(' ' * (w + 2))#输入，加保护圈
    y_1,x_1,y_2,x_2 = map(int,input().split())#和习惯不一样，所以两个坐标调换一下
    while x_1 + x_2 + y_1 + y_2 > 0:
        visited = [[False] * (w + 2) for _ in range(h + 2)]#记录已走过的路
        cur_path = [[x_1,y_1]]#用于记录路径
        step,min_step,flag = 0,0,False#flag用于判断是否可能找到目标
        dfs(x_1,y_1,x_2,y_2)
        if flag:
            print('Pair',str(cnt_pair)+':',str(min_step + 1),'segments.')
        else:
            print('Pair',str(cnt_pair)+':','impossible.')
        cnt_pair += 1
        y_1,x_1,y_2,x_2 = map(int,input().split())
    w,h = map(int,input().split())