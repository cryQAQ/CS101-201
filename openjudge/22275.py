class Treenode():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def buildtree(l):
    if l == []:
        return None
    root = Treenode(l[0])
    root.left = buildtree([x for x in l if x < l[0]])
    root.right = buildtree([x for x in l if x > l[0]])
    return root

def post(node):
    ans = []
    if node.left != None:
        ans += post(node.left)
    if node.right != None:
        ans += post(node.right)
    return ans + [node.val]

n = int(input())
print(' '.join(map(str,post(buildtree(list(map(int,input().split())))))))