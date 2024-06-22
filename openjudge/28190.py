N = int(input())
ans,stack = 0,[int(input())]
for _ in range(N - 1):
    n = int(input())
    if n <= stack[0]:
        ans = max(ans,len(stack))
        stack = [n]
    else:
        stack.append(n)
        if stack[-1] > stack[-2]:
            ans = max(ans,len(stack))
print(ans)
