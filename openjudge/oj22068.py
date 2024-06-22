origin = input()
while True:
    try:
        outout = input()
        stack,bank = [],list(origin)
        l = len(origin)
        flag = False
        if len(outout) == l:
            for i in range(l):
                if bank and not stack:
                    stack.append(bank.pop(0))
                while bank and stack[-1] != outout[i]:
                    stack.append(bank.pop(0))
                if stack.pop() != outout[i]:
                    print('NO')
                    flag = True
                    break
            if not flag:
                print('YES')
        else:
            print('NO')
    except EOFError:
        break