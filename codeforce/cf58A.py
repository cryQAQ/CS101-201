s = input()
H = s.find('h')
E = s.find('e',H+1)
L1 = s.find('l',E+1)
L2 = s.find('l',L1 + 1)
O = s.find('o',L2 + 1)
if int((H+1)*(E+1)*(L1+1)*(L2+1)*(O+1)) != 0:
    print('YES')
else:
    print('NO')
#compiled by cry_QAQ 2300011406 陈睿阳