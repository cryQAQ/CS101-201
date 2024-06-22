H = {'pop':0,'no':1,'zip':2,'zotz':3,'tzec':4,'xul':5,
    'yoxkin':6,'mol':7,'chen':8,'yax':9,'zac':10,'ceh':11,
    'mac':12,'kankin':13,'muan':14,'pax':15,'koyab':16,'cumhu':17,'uayet':18}
T = {'imix':1,'ik':2,'akbal':3,'kan':4,'chicchan':5,'cimi':6,
    'manik':7,'lamat':8,'muluk':9,'ok':10,'chuen':11,'eb':12,
    'ben':13,'ix':14,'mem':15,'cib':16,'caban':17,'eznab':18,'canac':19,'ahau':0}
n = int(input())
L = [n]
for _ in range(n):
    D,m,y = input().split()
    d = D[0]
    for i in range(1,len(D)-1):
        d = d + D[i]
    d = int(d)
    y = int(y)
    N = 365*y+20*H[m]+d+1
    key = list(T.keys())
    val = list(T.values())
    M = key[val.index(N%20)]
    if N%13 == 0:
        if N%260 == 0:
            L.append(str(13)+' '+M+' '+str(int(N/260)-1))
        else:
            L.append(str(13)+' '+M+' '+str(int(N/260)))
    else:
        L.append(str(N%13)+' '+M+' '+str(int(N/260)))
for i in range(len(L)):
    print(L[i])
#注意讨论边界情况