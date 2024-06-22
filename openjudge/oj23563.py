L = list(input().split('+'))
num = []
for i in range(len(L)):
    L[i] = L[i].split('^')
    L[i][0].lstrip('0')
    if ord(L[i][0][0]) >= ord('1') and ord(L[i][0][0]) <= ord('9'):
        num.append(int(L[i][1]))
print('n^'+str(sorted(num)[-1]))    