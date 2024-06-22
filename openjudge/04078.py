class heaplist:
    def __init__(self) -> None:
        self.heaplist=[-float("inf")]
        self.currentsize=0
    def percup(self,i):
        while self.heaplist[i]<self.heaplist[i//2]:
            self.heaplist[i],self.heaplist[i//2]=self.heaplist[i//2],self.heaplist[i]
            i=i//2
    def incert(self,k):
        self.heaplist.append(k)
        self.currentsize+=1
        self.percup(self.currentsize)
    def minchild(self,i):
        if i*2+1>self.currentsize or self.heaplist[i*2]<self.heaplist[i*2+1]:
            return i*2
        return i*2+1 
    def percdown(self,i):
        while i*2<=self.currentsize:
            mc=self.minchild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc]=self.heaplist[mc],self.heaplist[i]
            i=mc
    def delmin(self):
        retval=self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize-=1
        self.heaplist.pop()
        self.percdown(1)
        return retval
a=heaplist()
for _ in range(int(input())):
    x=list(map(int,input().split()))
    if x[0]==1:
        a.incert(x[1])
    else:
        print(a.delmin())