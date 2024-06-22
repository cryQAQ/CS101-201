import heapq
class Vertex:
    def __init__(self,val):
        self.val = val
        self.connect = {}
    def __lr__(self,other):
        return self.val < other.val

P = int(input())
graph = {}
for _ in range(P):
    s = input()
    graph[s] = Vertex(s)
Q = int(input())
for _ in range(Q):
    v_1,v_2,dis = input().split()
    graph[v_1].connect[graph[v_2]] = int(dis)
    graph[v_2].connect[graph[v_1]] = int(dis)

def dijk(start,end):
    q = []
    heapq.heapify(q)
    heapq.heappush(q,(0,start,start.val))
    while q:
        distance,node,path = heapq.heappop(q)
        if node == end:
            return path
        for next_node in node.connect.keys():
            heapq.heappush(q,(distance + node.connect[next_node],next_node,path + '->(' + str(node.connect[next_node]) + ')->' + next_node.val))
         
R = int(input())
for _ in range(R):
    start,end = input().split()
    print(dijk(graph[start],graph[end]))