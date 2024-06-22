def Poland(l):
    stk = []
    for num in l:
        if num == '+':
            a = float(stk.pop())
            b = float(stk.pop())
            stk.append(a + b)
        elif num == '-':
            a = float(stk.pop())
            b = float(stk.pop())
            stk.append(a - b)
        elif num == '*':
            a = float(stk.pop())
            b = float(stk.pop())
            stk.append(a * b)
        elif num == '/':
            a = float(stk.pop())
            b = float(stk.pop())
            stk.append(a / b)
        else:
            stk.append(float(num))
    return stk[0]
L = list(input().split())
L.reverse()
print("{:.6f}".format(Poland(L)))