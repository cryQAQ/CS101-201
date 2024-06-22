W = input()
L = []
N = []
ANS = str
for i in range(len(W)):
    L.append(W[i])
N.append(L[0].upper())
for i in range(1,len(W)):
    N.append(L[i])
ANS = N[0]
for i in range(1,len(W)):
    ANS = ANS + N[i]
print(ANS)
#1.知道了如何反过来将列表转为字符串，字符串转为列表需要先输入字符串后用for循环和.append()
#2.列表转为字符串需要用加法就可以了，前提是列表的每一项均为字符串
#3.当然，直接用title就可以解决这整个问题，但是这里相当于是把title重新写了一遍。
#4.还是要注意列表不能直接赋值，要用append。还是不熟练