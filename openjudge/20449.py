s = input()
num = 0
ans = ''
for i in range(len(s)):
    if s[i] == '1':
        num += 1
        num = num % 5
    if num == 0:
        ans += '1'
    else:
        ans += '0'
    num *= 2
print(ans)