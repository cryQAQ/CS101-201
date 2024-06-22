weight = {'A':0,'B':0,'C':0,'D':0,
          'E':0,'F':0,'G':0,'H':0,
          'I':0,'J':0,'K':0,'L':0}
apb = ['A','B','C','D','E','F',
       'G','H','I','J','K','L']
cpr = {'even':0,'up':-1,'down':+1}
N = int(input())
for _ in range(N):
        heavy_num = []
        light_num = []
        for i in range(12):
            heavy_num.append(0)
            light_num.append(0)
        for i in range(3):
            left,right,sit = input().split()
            for j in range(12):
                left_weight = 0
                right_weight = 0
                weight[apb[j]] = 1
                for k in range(4):
                    left_weight += weight[left[k]]
                    right_weight += weight[right[k]]
                if right_weight - left_weight == cpr[sit]:
                    heavy_num[j] += 1
                weight[apb[j]] = 0
            for j in range(12):
                left_weight = 0
                right_weight = 0
                weight[apb[j]] = -1
                for k in range(4):
                    left_weight += weight[left[k]]
                    right_weight += weight[right[k]]
                if right_weight - left_weight == cpr[sit]:
                    light_num[j] += 1
                weight[apb[j]] = 0
        if heavy_num.count(3) != 0:
            print(apb[heavy_num.index(3)]+' is the counterfeit coin and it is heavy.')
        elif light_num.count(3) != 0:
            print(apb[light_num.index(3)]+' is the counterfeit coin and it is light.')
