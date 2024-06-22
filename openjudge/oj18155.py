T = int(input())
S = list(map(int,input().split()))
l = len(S)
def dfs(S,step = 0):
    if step == l - 1:
        return [1,S[-1]]
    product = []
    for i in dfs(S,step + 1):
        product.append(i)
        product.append(i * S[step])
    return product
ans = dfs(S)
if T == 1 and not 1 in S:
    print('NO')
elif T in ans:
    print('YES')
else:
    print('NO')