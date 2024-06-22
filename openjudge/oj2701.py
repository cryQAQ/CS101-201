n = int(input())
ans = 0
for i in range(1,n + 1):
    if i % 7 != 0 and str(i).find('7') == -1:
        ans += i ** 2
print(ans)