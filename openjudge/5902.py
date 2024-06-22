class deque:
    def __init__(self):
        self.L = []
    def push(self,value):
        self.L.append(value)
    def pull(self,flag):
        if flag == 1:
            self.L.pop()
        else:
            self.L.pop(0)
    def __str__(self):
        if self.L:
            return ' '.join(map(str,self.L))
        else:
            return 'NULL'
N = int(input())
for _ in range(N):
    n = int(input())
    L = deque()
    for i in range(n):
        a,b = map(int,input().split())
        if a == 1:
            L.push(b)
        else:
            L.pull(b)
    print(L)