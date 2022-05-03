from sys import stdin


def Input_Data():
    readl = stdin.readline
    n = int(readl())
    plans = readl().strip().split(' ')
    return n, plans


def Move(n, plans):
    x, y, nx, ny = 1, 1, 1, 1 # x: row, y: col
    direction = {'R':(0, -1), 'L':(0, 1), 'U':(-1, 0), 'D':(1, 0)}

    for plan in plans:
        nx = x + direction[plan][0]
        ny = y + direction[plan][1]

        if nx<1 or ny<1 or nx>n or ny>n: continue
        x, y = nx, ny
    return x, y


print(*Move(*Input_Data()))