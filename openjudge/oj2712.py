DATE = {'1':0,'2':31,'3':59,'4':90,
        '5':120,'6':151,'7':181,'8':212,
        '9':243,'10':273,'11':304,'12':334}
N = int(input())
for _ in range(N):
    start_month,start_date,num,end_month,end_date = map(int,input().split())
    start_month = str(start_month)
    end_month = str(end_month)
    time = DATE[end_month] + end_date - DATE[start_month] - start_date
    print(num * (2 ** (time)))