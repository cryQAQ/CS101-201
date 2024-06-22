n = int(input())
L = sorted(list(map(int,input().split())))
goal = int(input())
i,j = 0,n - 1
flag = False
while i < j:
    if L[i] + L[j] > goal:
        j -= 1
    elif L[i] + L[j] < goal:
        i += 1
    else:
        print(str(L[i]),str(L[j]))
        flag = True
        break
if not flag:
    print('No')