class Treenode:
    def __init__(self,val):
        self.val = val
        self.child = [None] * 10
        self.is_end = False
flag = False
def trans(s,node):
    global flag
    if node.is_end:
        flag = True
    if len(s) >= 1:
        if not node.child[int(s[0])]:
            new_node = Treenode(int(s[0]))
            node.child[int(s[0])] = new_node
            new_node = trans(s[1:],new_node)
        else:
            node.child[int(s[0])] = trans(s[1:],node.child[int(s[0])])
    elif len(s) == 0:
        node.is_end = True
    return node
t = int(input())
for _ in range(t):
    n = int(input())
    L = []
    for _ in range(n):
        L.append(input())
    L = sorted(L)
    flag = False
    R = Treenode('R')
    for i in L:
        R = trans(i,R)
    print('NO' if flag else 'YES')