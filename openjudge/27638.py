class Treenode:
    def __init__(self):
        self.left = None
        self.right = None
def height(node):
    if node is None:
        return -1
    return max(height(node.left),height(node.right)) + 1
def count_leaves(node):
    if node == None:
        return 0
    if node.left == None and node.right == None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)
n = int(input())
nodes = [Treenode() for _ in range(n)]
no_parent = [True] * n
for i in range(n):
    l,r = map(int,input().split())
    if l != -1:
        nodes[i].left = nodes[l]
        no_parent[l] = False
    if r != -1:
        nodes[i].right = nodes[r]
        no_parent[r] = False
root = nodes[no_parent.index(True)]
print(height(root),count_leaves(root))

