n,m = map(int,input().split())
D = {}
for _ in range(m):
    DNA = input()
    for i in range(n):
        for j in range(i+1,n):
            if ord(DNA[i])>ord(DNA[j]):
                try:
                    D[DNA] += 1
                except:
                    D[DNA] = 1
key = list(D.keys())
val = list(D.values())
new = sorted(val)
for i in range(len(key)):
    print(key[val.index(new[i])])