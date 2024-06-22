from math import sqrt
def square_sum(n):
    flag = 0
    for i in range(1,int(sqrt(n / 2)) + 1):
        if int(sqrt(n - i ** 2)) == sqrt(n - i ** 2):
            return True
        else:
            flag += 1
    if flag == int(sqrt(n / 2)) + 1:
        return False
m = int(input())
l = list(map(int,input().split()))
for i in range(m):
    if square_sum(l[i]):
        print(bin(l[i]),oct(l[i]),hex(l[i]))