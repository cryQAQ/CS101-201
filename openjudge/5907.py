class Treenode:
    def __init__(self,val):
        self.val = val
        self.child = [None,None]
        self.parent = None
        self.label = None

def switch(x,y):
    L[x].parent.child[L[x].label], L[y].parent.child[L[y].label] = L[y],L[x]
    L[x].parent,L[y].parent = L[y].parent,L[x].parent
    L[x].label,L[y].label = L[y].label,L[x].label
    return

def search(node):
    if node.child[0] != None:
        return search(node.child[0])
    #if node.child[1] != None:
        #return search(node.child[1])
    return node.val
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    L = []
    for i in range(n):
        L.append(Treenode(i))
    for _ in range(n):
        a,b,c = map(int,input().split())
        if b != -1:
            L[b].parent = L[a]
            L[b].label = 0
            L[a].child[0] = L[b]
        if c != -1:
            L[c].parent = L[a]
            L[c].label = 1
            L[a].child[1] = L[c]
    for _ in range(m):
        l = list(map(int,input().split()))
        if l[0] == 1:
            switch(l[1],l[2])
        else:
            print(search(L[l[1]]))
    