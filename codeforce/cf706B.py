def binary(l,num):
    if num >= l[-1]:
        return len(l)
    elif num < l[0]:
        return 0
    else:
        left,right = 0,len(l) - 1
        while left < right :
            mid = (left + right) // 2
            if l[left] <= num and l[left + 1] > num:
                return left + 1
            elif l[mid] <= num:
                left = mid
            elif l[mid] > num:
               right = mid
n = int(input())
L = sorted(list(map(int,input().split())))
m = int(input())
for _ in range(m):
    s = int(input())
    print(binary(L,s))