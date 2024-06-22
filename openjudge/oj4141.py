weight = set()
a,b,c,d,e,f = map(int,input().split())
for A in range(a+1):
    for B in range(b+1):
        for C in range(c+1):
            for D in range(d+1):
                for E in range(e+1):
                    for F in range(f+1):
                        w = A * 1 + B * 2 + C * 3 + D * 5 + E * 10 + F * 20
                        if not(w in weight):
                            weight.add(w)
print('Total='+str(len(weight)-1))