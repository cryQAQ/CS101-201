class Treenode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right =None

def classify(s):
    S = set(s)
    if S == set('0'):
        return 'B'
    if S == set('1'):
        return 'I'
    return 'F'

def buildtree(s):
    node = Treenode(classify(s))
    if len(s) > 1:
        node.left = buildtree(s[:len(s) // 2])
        node.right = buildtree(s[len(s) // 2:])
    return node

def traversal(node):
    ans = ''
    if node.left:
        ans = traversal(node.left)
    if node.right:
        ans += traversal(node.right)
    return ans + node.value

N = int(input())
s = input()
print(traversal(buildtree(s)))