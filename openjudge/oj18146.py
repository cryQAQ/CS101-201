n,k = map(int,input().split())
l = list(map(int,input().split()))
cnt = [0] * 4
for i in l:
    cnt[i % 4] += 1
add = cnt[1] + cnt[3]
t = cnt[2] - 2 * n - cnt[1]
if t > 0:
    add += t * 2 // 3
    if t % 3 == 1:
        add += 2
    if t % 3 == 2:
        add += 4
print('YES'  if sum(l) + add <= n * 8 else 'NO')