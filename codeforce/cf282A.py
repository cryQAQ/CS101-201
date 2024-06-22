n = int(input())
P = []
x = 0
for i in range(n):
    P.append(input())
for i in range(n):
    if P[i][0] == '+' or P[i][2] == '+':
        x += 1
    else:
        x -= 1
print(x)
#compiled by 陈睿阳 2300011406