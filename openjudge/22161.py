
class TreeNode:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        self.left=None
        self.right=None

def preorder(Node,code):
    global dict
    if Node==None:
        return
    if len(Node.value)==1:
        dict[Node.value]=code
    preorder(Node.left,code+'0')
    preorder(Node.right,code+'1')
def decode(s):
    x=''
    if s=='':
        return ''
    for i in range(len(s)):
        if s[:i+1] in dict.values():
            x=new_dict[s[:i+1]]
            break
    return x+decode(s[i+1:])
def code(s):
    x=''
    for item in s:
        x+=dict[item]
    return x
n=int(input())
a,dict=[],{}
for _ in range(n):
    s,f=input().split()
    a.append(TreeNode(s,int(f)))
for _ in range(n-1):
    a.sort(key=lambda x:(x.weight,x.value[0]),reverse=True)
    x,y=a.pop(),a.pop()
    s=''.join(sorted(list(x.value)+list(y.value)))
    z=TreeNode(s,x.weight+y.weight)
    z.left,z.right=x,y
    a.append(z)
preorder(a[0],'')
new_dict = {v : k for k, v in dict.items()}
while True:
    try:
        s=input()
        if s.isdigit():
            print(decode(s))
        else :
            print(code(str(s)))
    except EOFError:
        break