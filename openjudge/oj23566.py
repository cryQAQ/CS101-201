n,m = map(int,input().split())
L = [0] * m
Coupon = []
total = 0
Price = []
for _ in range(n):
    shop,price = map(int,input().split())
    L[shop - 1] += price
for i in range(m):
    Coupon.append(list(map(int,input().split('-'))))
    if L[i] >= Coupon[-1][0]:
        Price.append(L[i] - Coupon[-1][1])
    else:
        Price.append(L[i])
    total += L[i]
print(int(sum(Price) - 30 * int((total / 200))))