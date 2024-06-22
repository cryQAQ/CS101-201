s = input()
t = input()
i = -1
j = -1
while s[i] == t[j]:
    if i+len(s)>0 and j+len(t)>0:
        i -= 1
        j -= 1
    elif i+len(s) == 0:
        j = -len(s)-2
        break
    elif j+len(t) == 0:
        i = -len(t)-2
        break
print(len(s)+len(t)+i+j+2)
#1.在进行多个数组同时操作的时候，需要注意项数不同导致的越界问题