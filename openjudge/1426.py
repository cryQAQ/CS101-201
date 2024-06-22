import queue
n = int(input())
while n != 0:
    l = queue.Queue()
    l.put(1)
    while not l.empty():
        m = l.get()
        if m % n == 0:
            print(m)
            break
        l.put(10 * m)
        l.put(10 * m + 1)
    n = int(input())