n = int(input())
l = []
for i in range(n):
    l.append(input())
for j in range(n):
    if len(l[j])<= 10:
        print(l[j])
    else:
        m = len(l[j])-2
        m = str(m)
        print(l[j][0]+m+l[j][-1])
#compiled by 2300011406 陈睿阳
#1.如何处理多行输入，知道了input实际上只会处理第一行的输入，就结束工作，这样可以利用循环和列表，将剩下的输入写入表格，同时，如果是一行有多个输入，可以使用split
#2.学会了len()的用法，用于数出字符串的长度
#3.学会了str()的用法，与“int()”相对应，可以把数字转化为字符串，不然格式不一样无法顺利输出
#4.熟练了string[i]和string[-1]的用法，用于得出第i个字符，应该内部就是相当于一个列表