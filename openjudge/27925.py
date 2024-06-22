from collections import deque, defaultdict
t = int(input())
team = defaultdict()
for i in range(t):
    for j in map(int,input().split()):
        team[j] = i
L = [[]for _ in range(t)]
sequence = deque()
s = input()
while s != 'STOP':
    if s[0] == 'E':
        a,num = s.split()
        num = int(num)
        if not L[team[num]]:
            sequence.append(team[num])
        L[team[num]].append(num)
    else:
        while not L[sequence[0]]:
            sequence.popleft()
        ans = L[sequence[0]].pop(0)
        print(ans)
    s = input()