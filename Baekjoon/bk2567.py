from sys import stdin
import time

canvas = [[0 for _ in range(101)] for _ in range(101)]
checker = ((-1, 0), (1, 0), (0, -1), (0, 1))

def Input_Data():
  readl = stdin.readline
  n = int(readl())
  
  for _ in range(n):
    x, y = map(int, readl().split(' '))
    for row in range(y, y+10):
      for col in range(x, x+10):
        canvas[row][col] = 1

  return n, canvas

def Solve(n, canvas):
  START_TIME = time.time()
  
  res = 0

  for row in range(101):
    for col in range(101):
      if canvas[row][col] == 1:
        for x, y in checker:
          if canvas[row+y][col+x] == 0:
            res += 1

  END_TIME = time.time()
  print("time: ", END_TIME - START_TIME)

  return res

N, canvas = Input_Data()
print(Solve(N, canvas))