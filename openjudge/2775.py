class treenode:
    def __init__(self,name,layer):
        self.name = name
        self.layer = layer
        self.childfile = []
        self.childdire = []
T = 1
root = treenode('ROOT',0)
parent_stack = [root]
space = '|     '
def gen_graph(node):
    l = node.layer
    ans = space * l + node.name + '\n'
    for d in node.childdire:
        ans += gen_graph(d)
    for f in sorted(node.childfile):
        ans += space * l + f +'\n'
    return ans

while True:
    s = input()
    if s == '#':
        break
    elif s != '*':
        if s[0] == 'f':
            parent_stack[-1].childfile.append(s)
        elif s[0] == 'd':
            new_node = treenode(s,parent_stack[-1].layer + 1)
            parent_stack[-1].childdire.append(new_node)
            parent_stack.append(new_node)
        elif s == ']':
            parent_stack.pop()
    else:
        print('DATA SET',str(T)+':')
        T += 1
        print(gen_graph(root))
        
        root = treenode('ROOT',0)
        parent_stack = [root]
