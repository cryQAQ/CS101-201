N = input()
L = []
ans = 0
for i in range(len(N)):
    L.append(N[i])
for i in range(1,len(N)):
    n = 0
    for j in range(0,i):
        if L[j] != L[i]:
            n += 1
            if n == i:
                ans += 1
if ans%2 == 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
#熟练了昨天学习的计数的方法