class treenode:
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None

def pre(node):
    ans = node.name
    if node.left:
        ans += pre(node.left)
    if node.right:
        ans += pre(node.right)
    return ans

def mid(node):
    ans = node.name
    if node.left:
        ans = mid(node.left) + ans
    if node.right:
        ans += mid(node.right)
    return ans

#未完成，看题解