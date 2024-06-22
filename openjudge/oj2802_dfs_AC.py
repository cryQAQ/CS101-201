import sys
sys.setrecursionlimit(100000)
def dfs(start,direction,seg,end):
    global temp,board,w,h,record
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    if start==end:
        temp=min(temp,seg)

    for i in range(4):
        nx=start[0]+dx[i]
        ny=start[1]+dy[i]
        if 0<=nx<=h+1 and 0<=ny<=w+1:
            if i!=direction:
                new_seg=seg+1
            else:
                new_seg=seg
            if new_seg>record[nx][ny]:
                continue
                
            if (nx,ny)==end:
                temp=min(temp,new_seg)
                continue
            
            if board[nx][ny]!="X":
                board[nx][ny]="X"
                record[nx][ny]=new_seg
                dfs((nx,ny),i,new_seg,end)
                board[nx][ny]=" "
    
    if temp==float('inf'):
        return -1
    else:
        return temp

num_board=0
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    num_board+=1
    print("Board #"+str(num_board)+":")
    board=[[" "]*(w+2)]
    for _ in range(h):
        board.append([" "]+list(input())+[" "])
    board.append([" "]*(w+2))
    output=[]
    num_pair=0
    while True:
        y1,x1,y2,x2=map(int,input().split())
        if x1==0:
            break
        num_pair+=1
        temp=float('inf')
        record=[[float('inf')]*(w+2) for i in range(h+2)]
        step=dfs((x1,y1),-1,0,(x2,y2))
        if step==-1:
            print("Pair "+str(num_pair)+": impossible.")
        else:
            print("Pair "+str(num_pair)+": "+str(step)+" segments.")
    print()