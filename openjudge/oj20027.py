a = input()
k = int(input())
l = len(a)
raw = 0
ans = str()
s = str()
for i in range(l):
    raw += (ord(a[i]) - ord('a')) * (26 ** (l - i - 1))

raw += k + 1
while raw:
    ans = chr(raw % 26 + 97) + ans
    raw //= 26
print('a' * (l - len(ans)) + ans)
