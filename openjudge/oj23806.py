L = sorted(list(map(int,input().split())))
l = len(L)
ans = set()
for i in range(l):
    j = i + 1
    k = l - 1
    while j < k:
        if L[i] + L[j] + L[k] > 0:
            k -= 1
        elif L[i] + L[j] + L[k] < 0:
            j += 1
        else:
            ans.add((L[i],L[j],L[k]))
            j += 1
            k -= 1
print(len(ans))