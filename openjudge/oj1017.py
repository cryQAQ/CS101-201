import math
Listc = [0,5,3,1]
while True:
    a,b,c,d,e,f = map(int,input().split())
    if a + b + c + d + e + f == 0:
        break
    N = f + e + d + math.ceil(c/4)
    if b > 5 * d + Listc[c%4]:
        N += math.ceil((b-(5 * d + Listc[c%4]))/9)
    if a > 36 * (N - f) -4 * b - 9 * c - 16 * d - 25 * e:
        a -= 36 * (N - f) -4 * b - 9 * c - 16 * d - 25 * e
        N += math.ceil((a)/36)
    print(N)