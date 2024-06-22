class Treenode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def ins(root, node):
    if node.name < root.name:
        if root.left:
            root.left = ins(root.left, node)
        else:
            root.left = node
    else:
        if root.right:
            root.right = ins(root.right,node)
        else:
            root.right = node
    return root

def buildtree(L):
    root = Treenode(L[0])
    for i in range(1,len(L)):
        for c in L[i]:
            new_node = Treenode(c)
            root = ins(root,new_node)
    return root

def pre(node):
    if not node:
        return ''
    return node.name + pre(node.left) + pre(node.right)

s = input()
L = [[]]
while s != '$':
    if s == '*':
        L.append([])
    else:
        L[-1].append(s)
    s = input()
for l in L:
    print(pre(buildtree(l[::-1])))