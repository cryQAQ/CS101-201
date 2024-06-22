A=['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 
   'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
B=['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 
   'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
C=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
D={}
for i in range(260):
    D[i]=C[i%13-1]+' '+B[i%20-1]
for _ in range(int(input())):
    a,b,c=input().split()
    a=int(a[:-1])
    c=int(c)
    n=365*c+A.index(b)*20+a+1
    print(D[n%260]+' '+str((n-1)//260))
