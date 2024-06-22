from collections import defaultdict
class Treenode:
    def __init__(self,value):
        self.parent = False
        self.value = value
        self.child = []

def traversal(node):
    global D
    ans = []
    v = node.value
    l = [v]
    for c in node.child:
        l.append(c.value)
    l.sort()
    for n in l:
        if n != v:
            ans += traversal(D[n])
        else:
            ans += [v]
    return ans

n = int(input())
D,S = defaultdict(),set()
for _ in range(n):
    l = list(map(int,input().split()))
    if len(l) != 1:
        parent,child = l[0],l[1:]
        c = []
        for i in child:
            if not i in S:
                c_i = Treenode(i)
                D[i] = c_i
                S.add(i)
            else:
                c_i = D[i]
            c_i.parent = True
            c.append(c_i)
        if not parent in S:
            S.add(parent)
            p = Treenode(parent)
            D[parent] = p
        else:
            p = D[parent]
        p.child = c
for i in S:
    if D[i].parent == False:
        root = D[i]
ans = traversal(root)
for _ in ans:
    print(_)