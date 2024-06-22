n = int(input())
L = []
D = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in range(n):
    L.append(input())
for i in range(n):
    c = int(L[i][0:2])
    y = int(L[i][2:4])
    month = int(L[i][4:6])
    date = int(L[i][6:])
    if month <= 2:
        if y != 0:
            month += 12
            y -= 1
        else:
            month += 12
            c -= 1
            y = 99
    w = (y+int(y/4)+int(c/4)-2*c+int(2.6*(month+1))+date-1)%7
    print(D[w])