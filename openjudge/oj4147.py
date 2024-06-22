def H(n,a,b,c):
    if n > 1:
        N = []
        N += H(n - 1,a,c,b)
        N.append(str(n)+':'+a+'->'+c)
        N += H(n - 1,b,a,c)
        return N
    else:
        return[str(1)+":"+a+'->'+c]
n,a,b,c = input().split()
n = int(n)
for i in range(len(H(n,a,b,c))):
    print(H(n,a,b,c)[i])