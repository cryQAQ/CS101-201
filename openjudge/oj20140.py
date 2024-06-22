import sys
sys.setrecursionlimit(100000)
s = input()
def scan(s):
    l = len(s)
    s = s[1:l - 1]#去除两端的括号
    l -= 2
    stack = []
    flag = [0]
    for i in range(l):#从前往后遍历
        stack.append(s[i])
        if s[i] == '[':
            flag[0] += 1
            flag.append(i)
        elif s[i] == ']':
            flag[0] -= 1
            if flag[0] == 0:#找到对应的后括号
                next = str()
                flag.append(i)
                for j in range(flag[1],flag[-1] + 1):#把这个括号中的内容提取出来
                    next += stack.pop()
                stack.append(scan(next[::-1]))#递归，并且把结果压入栈
                flag = [0]
    ans = str()
    for i in range(1,len(stack)):#处理数字
        ans += stack[i]
    return ans * int(stack[0])
if s[0] != '[':
    s = '[1' + s +']'
print(scan(s))