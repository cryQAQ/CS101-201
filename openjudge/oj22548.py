L = list(map(int,input().split()))
low,high,money =  L[0],L[0],0
choice = []
for i in range(len(L)):
    if L[i] > high:
        high = L[i]
        money = high - low
    elif L[i] < low:
        low = high = L[i]
        choice.append(money)
        money = 0
    else:
        choice.append(money)
print(max(choice))