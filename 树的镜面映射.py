import queue
class Treenode:
    def __init__(self,val):
        self.val = val
        self.child = []
        self.bro = []

class BinarytreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def mirror(node):
    node.child = node.child[::-1]
    for i in node.child:
        i = mirror(i)
    return node

def bfs(root):
    q = queue.Queue()
    ans = []
    q.put(root)
    while not q.empty():
        node = q.get()
        ans.append(node.val)
        for i in node.child:
            q.put(i)
    return ans
    
cur_root = []

def transform(node):#需要两个cur_root数组，节点只取决于其左子节点，在处理好左子节点之后把节点更新为其右子节点
    new_node = Treenode(node.val)
    cur_root.append(new_node)
    while node.left != None and node.left.val != '$':
        result = transform(node.left)
        new_node.child.append(result[0])
        if result[1] != None:
            node.left = result[1]
        else:node.left = None
    if node.right != None and node.right.val != '$':
        node = node.right
    else:
        node = None
    return new_node, node

def pre_order(R,l):
    global cur_root
    for i in l:
        new_binary_node = BinarytreeNode(i[0])
        if cur_root[-1].left == None:
            cur_root[-1].left = new_binary_node
        else:
            cur_root[-1].right = new_binary_node
            cur_root.pop()
        if i[1] == '0':
            cur_root.append(new_binary_node)
    return R

N = int(input())
L = list(input().split())

root = BinarytreeNode(L[0][0])
cur_root = [root]
root = pre_order(root, L[1:])
new_root = transform(root)[0]
new_root = mirror(new_root)
print(*bfs(new_root))
