class treenode:
    def __init__(self,value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

def insert(num,node):
    if node == None:
        return treenode(num)
    if node.value > num:
        node.leftchild = insert(num,node.leftchild)
    elif node.value < num:
        node.rightchild = insert(num,node.rightchild)
    return node

def treverse(node):
    queue = [node]
    traversal = []
    while queue:
        node = queue.pop(0)
        traversal.append(node.value)
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)
    return traversal

L = list(map(int,input().split()))
root = treenode(L[0])
for i in range(1,len(L)):
    insert(L[i],root)
print(' '.join(map(str,treverse(root))))