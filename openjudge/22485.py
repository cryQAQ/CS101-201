import queue
class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = False
        self.right = False
        self.depth = 0

def cal_dep(node):
    if node.left:
        node.left.depth = node.depth + 1
        cal_dep(node.left)
    if node.right:
        node.right.depth = node.depth + 1
        cal_dep(node.right)
    return

def traveral(root):
    q = queue.Queue()
    ans = [0] * N
    q.put(root)
    while not q.empty():
        node = q.get()
        ans[node.depth] = node.val
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return ans
N = int(input())
L = [Treenode(i) for i in range(1,N + 1)]
for i in range(N):
    a,b = map(int,input().split())
    if a != -1:
        L[i].left = L[a - 1]
    if b != -1:
        L[i].right = L[b - 1]
cal_dep(L[0])
print(' '.join(map(str,[i for i in traveral(L[0]) if i != 0])))