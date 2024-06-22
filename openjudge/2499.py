def num(l,r):
    if l > r:
        a_1,a_2 = num(l - r,r)
        return a_1 + 1, a_2
    if l < r:
        a_1,a_2 = num(l,r - l)
    if l == r:
        if l == 1:
            return 0,0
        a_1,a_2 = num(l - 1,r)
        return a_1