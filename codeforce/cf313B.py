s = input()
L = [0]
num = 0
for i in range(1,len(s)):
    if s[i] == s[i - 1]:
        num += 1
    L.append(num)
m = int(input())
for _ in range(m):
    i,j = map(int,input().split())
    print(L[j - 1] - L[i - 1])