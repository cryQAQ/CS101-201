n = int(input())
r = list(map(int,input().split()))
R = [[r[0]]]
total = n
for i in range(1,len(r)):
    if r[i] != R[-1][-1]:
        R[-1].append(r[i])
    else:
        R.append([r[i]])  
for _ in range(len(R)):
    m = len(R[_])
    if m > 1:
        flag,candy,top,bot = [0] * m,[0] * m,[],[]
        for i in range(1,m - 1):
            if R[_][i + 1] > R[_][i] and R[_][i - 1] > R[_][i]:
                flag[i] = -1
                bot.append(i)#找到最低点
            elif R[_][i + 1] < R[_][i] and R[_][i - 1] < R[_][i]:
                flag[i] = 1
                top.append(i)#找到最高点
        for i in bot:
            j_1,j_2 = 1,1
            while i + j_1 <= m - 1 and flag[i + j_1] != 1:
                candy[i + j_1] = j_1
                j_1 += 1
            while i - j_2 >= 0 and flag[i - j_2] != 1:
                candy[i - j_2] = j_2
                j_2 += 1#最低点向两边推
        for i in top:
            j_1,j_2 = 1,1
            while i + j_1 < m - 1 and flag[i + j_1] != -1:
                j_1 += 1
            while i - j_2 > 0 and flag[i - j_2] != -1:
                j_2 += 1
            candy[i] = max(j_1,j_2)#定义最高点的值
        if flag.count(1) > 0 and flag.count(-1) > 0:#解决整个数列的头尾两端的边界问题
            if flag.index(1) < flag.index(-1):
                for i in range(flag.index(1)):
                    candy[i] = i
            flag.reverse()
            if flag.index(1) < flag.index(-1):
                for i in range(flag.index(1)):
                    candy[m - i - 1] = i
        elif flag.count(1) > 0:
            for i in range(flag.index(1)):
               candy[i] = i
            flag.reverse()
            for i in range(flag.index(1)):
                candy[m - i - 1] = i
        elif flag.count(1) == 0 and flag.count(-1) == 0:
            if R[_][1] > R[_][0]:
                for i in range(m):
                    candy[i] = i
            else:
                for i in range(m):
                    candy[i] = (m - i - 1)
        total += sum(candy)
print(total)
#总体思路是找到极大值和极小值，将其切分成几段单调序列，然后最低点设为零，然后两边推，依次递增