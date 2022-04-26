from sys import stdin
import time

canvas = [[0 for _ in range(100)] for _ in range(100)]


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

  for row in canvas:
	  res += sum(row)

  END_TIME = time.time()
  print("time: ", END_TIME - START_TIME)

  return res

N, canvas = Input_Data()
print(Solve(N, canvas))