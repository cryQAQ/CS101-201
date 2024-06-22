import queue
A,B,C = map(int,input().split())
def bfs():
    q = queue.Queue()
    q.put((0,0,[]))
    visited = set()
    while not q.empty():
        stat_1,stat_2,move = q.get()
        if stat_1 == C or stat_2 == C:
            return move
        visited.add((stat_1,stat_2))
        if (0,stat_2) not in visited:
            q.put((0,stat_2,move + ['DROP(1)']))
        if (stat_1,0) not in visited:
            q.put((stat_1,0,move + ['DROP(2)']))
        if (A,stat_2) not in visited:
            q.put((A,stat_2,move + ['FILL(1)']))
        if (stat_1,B) not in visited:
            q.put((stat_1,B,move + ['FILL(2)']))
        if stat_1 + stat_2 < B:
            if (0,stat_1 + stat_2) not in visited:
                q.put((0,stat_1 + stat_2,move + ['POUR(1,2)']))
        else:
            if (stat_1 + stat_2 - B) not in visited:
                q.put((stat_1 + stat_2 - B,B,move + ['POUR(1,2)']))
        if stat_1 + stat_2 < A:
            if (stat_1 + stat_2,0) not in visited:
                q.put((stat_1 + stat_2,0,move + ['POUR(2,1)']))
        else:
            if (A,stat_1 + stat_2 - A) not in visited:
                q.put((A,stat_1 + stat_2 - A,move + ['POUR(2,1)']))
    return False
ans = bfs()
if not ans:
    print('impossible')
else:
    print(len(ans))
    for i in ans:
        print(i)