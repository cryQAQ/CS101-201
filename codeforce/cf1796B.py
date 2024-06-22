N  = int(input())
ANS = []
for i in range(N):
    a = input()
    b = input()
    if a[0] == b[0]:#判断首位是否一致
        ANS.append('YES')
        ANS.append(str(a[0])+'*')
    elif a[-1] == b[-1]:#判断末尾是否一致
        ANS.append('YES')
        ANS.append('*'+str(a[-1]))
    else:#如果首位和末位都不一致，则必须有相邻一致才可行
        n = 0
        for j in range(len(a)-1):
            for k in range(len(b)-1):
                if a[j] == b[k] and a[j+1] == b[k+1]:#判断是否存在相邻一致
                    ANS.append('YES')
                    ANS.append('*'+str(a[j])+str(a[j+1])+'*')
                    n = 1
                    break
            if n > 0:#使一对有不止两个相邻字母一致的单词只输出一次
                break
        if n == 0:#没有相邻字母一致的，输出NO
            ANS.append('NO')
for i in range(len(ANS)):
    print(ANS[i])
#附两个AC代码
#t=int(input())
#f=[]
#for i in range(0,t):
    #a=input()
    #b=input()
    #f.append([a,b])
#for i in range(0,t):
    #a,b=f[i][0],f[i][1]
    #m,n=len(f[i][0]),len(f[i][1])
    #if a[0]==b[0] :
        #print("YES")
        #print(a[0]+"*")
    #elif a[m-1]==b[n-1]:
        #print("YES")
        #print("*"+a[m-1])
    #else:
        #x=0
        #for j in range(0,m-1):
            #if not b.find(a[j]+a[j+1])==-1:
                #x=1
                #print("YES")
                #print("*"+a[j]+a[j+1]+"*")
                #break
        #if x==0:
            #print("NO")
#