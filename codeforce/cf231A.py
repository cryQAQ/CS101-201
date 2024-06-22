n = int(input())
a = 0
b = 0
c = 0
m = 0
for i in range(n):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a == 1 and b == 1:
        m += 1
    elif a == 1 and c == 1:
        m += 1
    elif b == 1 and c == 1:
        m += 1
print(m)
#1.注意不重复命名
#2.这里不能直接令数组的第i个是多少
#3.不能类似a,b,c = 0来赋值，必须分开打