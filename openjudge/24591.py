def infix_to_ans(mid):
    order = {'+': 1, '-': 1, '*': 2, '/': 2}

    stack = []
    ans = []

    for i in range(len(mid)):
        if mid[i] == '(':
            stack.append(mid[i])
        elif mid[i] == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        elif mid[i] in '+-*/':
            while stack and stack[-1] != '(' and order[mid[i]] <= order[stack[-1]]:
                ans.append(stack.pop())
            stack.append(mid[i])
        else:
            if mid[i - 1] in '+-*/()' or not ans:
                ans.append(mid[i])
            else:
                ans[-1] += mid[i]

    while stack:
        ans.append(stack.pop())

    return ' '.join(ans)

n = int(input())
for _ in range(n):
    print(infix_to_ans(input()))