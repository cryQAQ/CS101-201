while True:
    n,m = map(int,input().split())
    check = []
    check.append(1)
    if n == 0 and m == 0:
        break
    for _ in range(n):  
        check.append(0)
    i,j = 0,0
    while True: 
        if sum(check) == len(check):
            break
        else:
            if check[i%n+1] == 0:
                j += 1
                i += 1
                if j == m:
                    if i%n != 0:
                        check[i%n] = 1
                        ans = i%n
                        j = 0
                    else:
                        check[n] = 1
                        ans = n
                        j = 0
            else:
                i += 1
    print(ans)