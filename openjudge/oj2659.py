A,B,K = map(int,input().split())
L = []
num = 0
for _ in range(K):
    L.append(list(map(int,input().split())))
for i in range(A):
    for j in range(B):
        flag = 0
        for k in range(K):
            R = int((L[k][2]-1)/2)
            if abs(i - L[k][0] + 1) <= R and abs(j - L[k][1] + 1) <= R and L[k][3] == 1:
                flag += 1
            elif abs(i - L[k][0] + 1) > R and L[k][3] == 0 or abs(j - L[k][1] + 1) > R and L[k][3] == 0:
                flag += 1
        if flag == K:
            num += 1
print(num)
