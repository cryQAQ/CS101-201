N = int(input())
x = []
y = []
for i in range(N):
    X,Y = input().split()
    X = float(X)
    Y = float(Y)
    x.append(X)
    y.append(Y)
for i in range(N):
    S = 0
    while S < 0.5*3.1415*(x[i] ** 2 + y[i] ** 2):
        S += 50
        year = S/50
        year = int(year)
    print("Property "+str(i+1)+": This property will begin eroding in year "+str(year),end=".\n")
print("END OF OUTPUT.")
