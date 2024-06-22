N = int(input())
for _ in range(N):
    F = [1,1]
    num = int(input())
    if num == 1 or num == 2:
        print('1')
    else:
        for i in range(num - 2):
            F.append(F[-1]+F[-2])
        print(F[-1])