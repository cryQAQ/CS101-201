n = int(input())
m = 0
for i in (4,7,47,74,444,474,477,744,747,774,777):
    if n%i == 0:
        print("YES")
        m += 1
        break
if m == 0:
    print('NO')
#灵活实用for循环