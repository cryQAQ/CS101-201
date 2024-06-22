s = input()
m = 0
n = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        m += 1
    else:
        m = 0
    if m == 6:
        print('YES')
        n = 1
        break
if n == 0:
    print('NO')
#compiled by 陈睿阳 2300011406