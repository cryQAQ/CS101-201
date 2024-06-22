n = int(input())
number, Number, count = [], ['0'], [0]
tinydict = {}
for i in range(n):
    str = input().split('-')#以-为分隔符分割字符串
    for j in range(len(str)):
        str[j] = list(str[j].upper())
        for k in range(len(str[j])):#将字母转换为数字
            if str[j][k] >= 'A' and str[j][k] <= 'C':
                str[j][k] = '2'
            elif str[j][k] >= 'D' and str[j][k] <= 'F':
                str[j][k] = '3'
            elif str[j][k] >= 'G' and str[j][k] <= 'I':
                str[j][k] = '4'
            elif str[j][k] >= 'J' and str[j][k] <= 'L':
                str[j][k] = '5'
            elif str[j][k] >= 'M' and str[j][k] <= 'O':
                str[j][k] = '6'
            elif str[j][k] >= 'P' and str[j][k] <= 'S':
                str[j][k] = '7'
            elif str[j][k] >= 'T' and str[j][k] <= 'V':
                str[j][k] = '8'
            elif str[j][k] >= 'W' and str[j][k] <= 'Z':
                str[j][k] = '9'
    number.append(''.join(str[j]))
    number[i] = number[i][:3] + '-' + number[i][3:]#将电话号按标准形式储存
    for j in range(len(Number)):#统计电话号码出现次数
        if number[i] not in Number:
            Number.append(number[i])
            tinydict[Number[len(Number)-1]] = 1
            break
        elif number[i]  ==  Number[j]:
            tinydict[Number[j]] += 1
            break

Number.sort()
for i in range(1,len(Number)):
    print(Number[i], tinydict[Number[i]])
    



    