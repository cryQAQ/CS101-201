n = int(input())
for _ in range(n):
    angle = int(input())
    num = 0
    for i in range(1,int(2/(1-angle/180))+2):
        if 180 * (i - 2) == angle * i:
            print('YES')
            num += 1
            break
    if num == 0:
        print('NO')
#compiled by 陈睿阳 2300011406