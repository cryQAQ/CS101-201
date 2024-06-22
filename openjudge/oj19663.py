n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [ sum(map(int,i.split(','))) for i in pairs]
prices = list(map(int,input().split()))
efficiency = []
for i in range(n):
    efficiency.append(distances[i]/prices[i])
ans = 0
if n % 2 == 1:
    e_m = sorted(efficiency)[(n - 1) // 2]
    p_m = sorted(prices)[(n - 1) // 2]
else:
    e_m = (sorted(efficiency)[n // 2 - 1] + sorted(efficiency)[n // 2]) / 2
    p_m = (sorted(prices)[n // 2 - 1] + sorted(prices)[n // 2]) / 2
for i in range(n):
    if efficiency[i] > e_m and prices[i] < p_m:
        ans += 1
print(ans)