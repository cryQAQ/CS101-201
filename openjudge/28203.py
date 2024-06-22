n = int(input())
L = list(map(int,input().split()))
mono_stack,ans = [(L[0],0)],[0] * n
for i in range(1,n):
    while mono_stack and mono_stack[-1][0] < L[i]:
        ans[mono_stack[-1][1]] = i + 1
        mono_stack.pop()
    mono_stack.append((L[i],i))
print(*ans)