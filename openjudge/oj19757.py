while True:
    R,n = map(int,input().split())
    while R == -1 and n == -1:
        break
    X = sorted(list(set(map(int,input().split()))))
    i = 0
    ans = 1
    while i < len(X):
        for j in range(i+1,len(X)):
            if j != len(X) - 1:
                if X[j] <= X[i] + R and X[j+1] > X[i] + R:
                    ans += 1
                    for k in range(j+1,len(X)):
                        if X[k] <= X[j] + R and X[k+1] > X[j] +R:
                            i = k + 1
                            break
                        else:
                            i = j + 1
                            break
                    break
            else:
                ans += 1
                i = len(X)
                break
    print(ans)