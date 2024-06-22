triangle = [None] * 11
def tri(n):
    global triangle
    if n == 1:
        ans = [[' ','/','\\',' '],
               ['/','_','_','\\']]
        triangle[1] = ans
        return ans
    s = tri(n - 1)
    b = [' '] * (2 ** (n - 1))
    ans = []
    for l in s:
        ans.append(b + l + b)
    for l in s:
        ans.append(l * 2)
    triangle[n] = ans
    return ans
a = tri(10)
n = int(input())
while n != 0:
    ans = triangle[n]
    for j in range(len(ans)):
        if j != len(ans) - 1:
            print(''.join(ans[j]))
        else:
            print(''.join(ans[j]) + '\n')
    n = int(input())