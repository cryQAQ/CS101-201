n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if c%2 == 0:
        if a > b:
            print('First')
        else:
            print('Second')
    else:
        if a >= b:
            print('First')
        else:
            print('Second')
