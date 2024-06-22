L = []
for i in range(2):
    L.append(input())
a = L[0].upper()
b = L[1].upper()
A,B = 0,0
n = 0
for i in range(len(a)):
    if ord(a[i])>ord(b[i]):
        print(1)
        break
    elif ord(a[i])<ord(b[i]):
        print(-1)
        break
    else:
        n += 1
if n == len(a):
    print(0)
#compiled by 2300011406 陈睿阳
#1.没有理解比较字符串大小的规则：从左往右开始，每一个字符逐个比较其ASCII编码，直至出现第一个不同，哪个编码大哪个就大
#2.可以简写为：
# a=input().lower()
# b=input().lower()即可，不需要先弄进一个列表，他可以自己读出两行的内容
#3.不仅仅只有while可以break，if也可以在for里面break