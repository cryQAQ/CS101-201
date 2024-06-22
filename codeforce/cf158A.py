n,k = input().split()
n = int(n)
k = int(k)
S = []
m = 0
j = 0
l = 0
S.extend(input().split())
for i in range(n):   
    S[i] = int(S[i])
if S[k-1] > 0:
    while S[j] >= S[k-1]:
        m += 1
        j += 1
        if j == n:
            break
    print(m)
else:
    while S[l] > 0:
        m += 1
        l += 1
        if l == n:
            break
    print(m)
#compiled by 2300011406 陈睿阳
#1.如何在一行中读取不确定个数的数据，不能使用split.()而是用extend
#2。注意第i项是S[i-1]而不是S[i]这一点很容易错
#3.需要注意上限，注意边界情况会不会溢出。