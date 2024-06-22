s = input()
L = []
for i in range(int((len(s)+1)/2)):
    L.append(s[2*i])
L.sort()
for i in range(len(L)):
    L[i] = str(L[i])
for i in range(int((len(s)-1)/2)):
    L.insert(2*i+1,'+')
ans = L[0]
for i in range(1,len(L)):
    ans = ans + str(L[i])
print(ans)