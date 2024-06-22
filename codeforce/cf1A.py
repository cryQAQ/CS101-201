import math
m,n,a = input().split()
m = int(m)
n = int(n)
a = int(a)
M = math.ceil(m/a)
N = math.ceil(n/a)
print(M*N)
#原来想用while手写向上取整，但是由于数据过大，会超时，因此使用ceil函数
#学会使用math库，向上取整为math.ceil();向下取整为math.floor;向0取整是int;四舍五入是round();还有整除，等于先相除再想下取整为//,方法为a//b