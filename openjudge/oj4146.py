n = int(input())
L = []
for a_3 in range(n,-1,-1):
    for a_2 in range(n,-1,-1):
        if (a_2 + a_3) % 3 == 0:
            for a_1 in range(n,-1,-1):
                if (a_1 + a_2) % 2 == 0 and (a_1 + a_2 + a_3) % 5 == 0:
                    L.append(a_1 + a_2 + a_3)
                    break
L.sort()
print(L[-1])