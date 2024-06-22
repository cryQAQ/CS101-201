class Treenode:
    def __init__(self,name):
        self.name = name
        self.child = []

def pre(root):
    ans = root.name
    if root.child:
        for node in root.child:
            ans += pre(node)
    return ans

def post(root):
    ans = ''
    if root.child:
        for node in root.child:
            ans += post(node)
    return ans + root.name

nodes = []
parent_stack = []
s = input()
for c in s:
    if ord('A') <= ord(c) <= ord('Z'):
        new_node = Treenode(c)
        nodes.append(new_node)
        if parent_stack:
            parent_stack[-1].child.append(new_node)
    elif c == '(':
        parent_stack.append(nodes[-1])
    elif c == ')':
        parent_stack.pop()
print(pre(nodes[0]))
print(post(nodes[0]))