class Treenode:
    def __init__(self, val):
        self.val = val
        self.child = []

class Binarytreenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def depth(tree_node):
    ans = -1
    if tree_node.child:
        for i in tree_node.child:
            ans = max(ans,depth(i))
    return ans + 1

def binary_depth(node):
    ans = -1
    if node.left:
        ans = max(ans,binary_depth(node.left))
    if node.right:
        ans = max(ans, binary_depth(node.right))
    return ans + 1

def buildtree(s):
    cnt = 0
    root = Treenode(cnt)
    cur_root = [root]
    for i in s:
        if i == 'd':
            cnt += 1
            new_node = Treenode(cnt)
            cur_root[-1].child.append(new_node)
            cur_root.append(new_node)
        else:
            cur_root.pop()
    return root

def transform(node,brother):
    new_node = Binarytreenode(node.val)
    if len(node.child) > 1:
        new_node.left = transform(node.child[0],node.child[1:])
    elif len(node.child) == 1:
        new_node.left = Binarytreenode(node.child[0].val)
    if len(brother) >= 1:
        next_node = brother.pop(0)
        new_node.right = transform(next_node,brother)
    return new_node

origin_root = buildtree(input())
new_root = transform(origin_root,[])
d_1,d_2 = depth(origin_root), binary_depth(new_root)
print(str(d_1) + ' => ' + str(d_2))
        
