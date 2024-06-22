d = int(input())
n = int(input())
street = [[0] * 1025 for _ in range(1025)]
for _ in range(n):
    x,y,num = map(int,input().split())
    for i in range(max(0,x - d),min(1025,x + d + 1)):
         for j in range(max(0,y - d),min(1025,y + d + 1)):
              street[i][j] += num
amount = 0
N = 0
for i in range(1025):
    for j in range(1025):
            if amount < street[i][j]:
                 amount = street[i][j]
                 N = 1
            elif amount == street[i][j]:
                 N += 1
print(N,amount)