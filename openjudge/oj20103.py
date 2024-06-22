from copy import deepcopy
N = input()
l = len(N)
def dfs(s,n):
    if n == 1:
        return['',s]
    ans = []
    for i in dfs(s[1:],n - 1):
        ans.append(i)
        ans.append(s[0] + i)
    return ans
def flag(N,l):
    L = deepcopy(dfs(N,l))
    L.remove('')
    for i in L:
        if int(i) % 7 == 0:
            return 'YES'
    return 'NO'
if l >= 7:
    print('YES')
else:
    print(flag(N,l))