n = int(input())
D = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,
     'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'R':7,'S':7,
     'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9}
L = []
l = []
a = 0
for _ in range(n):
    s = input()
    num = str()
    for i in range(len(s)):
        if s[i] != '-':
            if ord(s[i]) >= ord('A'):
                num += str(D[s[i]])
            else:
                num += str(s[i])
    L.append(num)
L.sort()
if len(set(L)) == len(L):
    print('No duplicates.')
else:
    d = {}
    for i in L:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if d[L[0]] != 1:
        print(str(L[0][0:3])+'-'+str(L[0][3:7])+' '+str(d[L[0]]))
    for i in range(1,len(L)):
        if L[i] != L[i-1] and d[L[i]] != 1:
            print(str(L[i][0:3])+'-'+str(L[i][3:7])+' '+str(d[L[i]]))
#1.学会使用dict
#2。学会自己不用count,节省时间，使用dict来计数
