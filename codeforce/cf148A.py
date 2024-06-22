import math
I = []
for i in range(4):
    I.append(int(input()))
lim = int(input())
L_0 = []
L_1 = []
L_2 = []
L_3 = []
F = []
if lim%I[0] == 0:
    for i in range(1,math.ceil(lim/I[0])+1):
        L_0.append(i*I[0])
else:
    for i in range(1,math.ceil(lim/I[0])):
        L_0.append(i*I[0])
if lim%I[1] == 0:
    for i in range(1,math.ceil(lim/I[1])+1):
        L_1.append(i*I[1])
else:
    for i in range(1,math.ceil(lim/I[1])):
        L_1.append(i*I[1])
if lim%I[2] == 0:
    for i in range(1,math.ceil(lim/I[2])+1):
        L_2.append(i*I[2])
else:
    for i in range(1,math.ceil(lim/I[2])):
        L_2.append(i*I[2])
if lim%I[3] == 0:
    for i in range(1,math.ceil(lim/I[3])+1):
        L_3.append(i*I[3])
else:
    for i in range(1,math.ceil(lim/I[3])):
        L_3.append(i*I[3])
for i in range(len(L_0)):
    F.append(L_0[i])
for i in range(len(L_1)):
    n = 0
    for j in range(len(F)):
        if L_1[i] != F[j]:
            n +=1
    if n == len(F):
        F.append(L_1[i])
for i in range(len(L_2)):
    n = 0
    for j in range(len(F)):
        if L_2[i] != F[j]:
            n +=1
    if n == len(F):
        F.append(L_2[i])
for i in range(len(L_3)):
    n = 0
    for j in range(len(F)):
        if L_3[i] != F[j]:
            n +=1
    if n == len(F):
        F.append(L_3[i])
print(len(F))