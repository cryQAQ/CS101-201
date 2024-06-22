n = int(input())
L = []
L.extend(input().split())
for i in range(len(L)):
    L[i] = int(L[i])
C = L.copy()
L.sort()
A = []
A.append(L[0])
for i in range(1,len(L)):
    if L[i] != A[-1]:
        A.append(L[i])
    if len(A) == 3:
        break
if len(A) < 3:
    print('-1 -1 -1')
else:
    print(str(C.index(A[0])+1)+' '+str(C.index(A[1])+1)+' '+str(C.index(A[2])+1))
#1.学会了index的用法
#2.要把列表元素转为int，需要用extend来加入而不是append