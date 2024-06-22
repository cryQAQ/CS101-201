import copy
import sys
sys.setrecursionlimit(1000000) 
def main():
    a = 0
    while True:
        a += 1
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        print(f"Board #{a}:")

        lst = [[1 for _ in range(w+4)]]
        lst1 = [1]
        for _ in range(w+2):
            lst1.append(0)
        lst1.append(1)
        lst.append(list(lst1))
        for _ in range(h):
            lst2 = [1, 0]
            str1 = input()
            for c in str1:
                if c == "X":
                    lst2.append(1)
                else:
                    lst2.append(0)
            lst2.append(0)
            lst2.append(1)
            lst.append(list(lst2))
        lst.append(list(lst1))
        lst.append([1 for _ in range(w+4)])

        b = 0
        while True:
            b += 1  
            x1, y1, x2, y2 = map(lambda x: int(x)+1, input().split())
            if x1 == 1 and y1 == 1 and x2 == 1 and y2 == 1:
                print()
                break

            state = copy.deepcopy(lst)
            state[y2][x2] = 0
            global turn_final
            turn_final = 1000000

            walk(state, -1, 0, y1, x1, y2, x2)

            if turn_final != 1000000:
                print(f"Pair {b}: {turn_final} segments.")
            else:
                print(f"Pair {b}: impossible.")


def walk(state, direction, turn, y1, x1, y2, x2):
    global turn_final
    dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    if turn == turn_final:
        return
    for d in range(4):
        x = x1 + dire[d][0]
        y = y1 + dire[d][1]
        if state[y][x] == 0:
            state[y][x] = 1
            if d != direction:
                t = 1
            else:
                t = 0
            if x == x2 and y == y2:
                turn_final = min(turn_final, turn+t)
                state[y][x] = 0
            else:
                walk(state, d, turn+t, y, x, y2, x2)
                state[y][x] = 0


if __name__ == "__main__":
    main()