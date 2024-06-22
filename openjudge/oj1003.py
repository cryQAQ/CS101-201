L = [1]
n = 0
while L[n] != 0.00:
    L.append(float(input()))
    n += 1
for i in range(1,len(L)-1):
        S = 0
        j = 1
        while S < L[i]:
            S += 1/(j+1)
            j += 1
        print(j-1,end=' card(s)\n')
#1.学会如何在没有提示行数的情况下，得到多行输入的结果