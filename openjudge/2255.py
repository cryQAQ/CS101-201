class BinaryTreeNode:
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None

def buildtree(s_1,s_2):
    if len(s_1) > 1:
        root_node = BinaryTreeNode(s_1[0])
        mid_i = s_2.index(s_1[0])
        pre_i = s_1.index(s_2[mid_i - 1])
        next_mid_left,next_mid_right = s_2[:mid_i],s_2[mid_i + 1:]
        next_pre_left,next_pre_right = s_1[1:pre_i + 1],s_1[pre_i + 1:]
        root_node.left = buildtree(next_pre_left,next_mid_left)
        root_node.right = buildtree(next_pre_right,next_mid_right)
        return root_node
    if len(s_1) == 1:
        return BinaryTreeNode(s_1)
    if len(s_1) == 0:
        return None

def post(node):
    ans = ''
    if node.left:
        ans += post(node.left)
    if node.right:
        ans += post(node.right)
    ans += node.name
    return ans

while True:
    try:
        s_1,s_2 = input().split()
        print(post(buildtree(s_1,s_2)))
    except EOFError:
        break