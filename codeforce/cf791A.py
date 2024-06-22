L,B = map(int,input().split())
year = 0
while L <= B:
    L = 3*L
    B = 2*B
    year += 1
print(year)
