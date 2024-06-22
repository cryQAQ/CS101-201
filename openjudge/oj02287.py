n = int(input())
while n > 0:
    general = sorted(list(map(int,input().split())),reverse=True)
    king = sorted(list(map(int,input().split())),reverse=True)
    win,g_first,g_last,k_first,k_last = 0,0,n - 1,0,n - 1
    while g_first <= g_last:
        while g_first <= g_last and general[g_first] > king[k_first]:
            win += 1
            g_first += 1
            k_first += 1
        while g_first <= g_last and general[g_last] > king[k_last]:
            win += 1
            g_last -= 1
            k_last -= 1
        if g_first <= g_last and general[g_last] < king[k_first]:
            win -= 1
            g_last -= 1
            k_first += 1
        else:
            break
    print(win * 200)
    n = int(input())