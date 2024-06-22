ans = []
def dfs(A,cur = 0):
    if cur == len(A):
        ans.append(''.join([str(x + 1) for x in A]))
        return
    for col in range(len(A)):
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
        else:
            A[cur] = col
            dfs(A,cur + 1)
dfs([None] * 8)
for _ in range(int(input())):
    print(ans[int(input()) - 1])