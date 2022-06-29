import sys
from collections import deque
import pygame
import numpy as np
import random
sys.setrecursionlimit(10**5)

pygame.init()

# constants
DISP_WIDTH = 1024
DISP_HEIGHT = 768
CELL_SIZE = 5

speed = 120 # frames per sec

gray = (100, 100, 100)  # undiscovered node or edge
white = (255, 255, 255)  # discovered edge or node outline
yellow = (200, 200, 0)  # current node fill
red = (200,0,0) # discovered node fill
black = (0, 0, 0)  # undiscovered node fill
blue = (50,50,160) # completed node fill and completed edge

screen = pygame.display.set_mode([DISP_WIDTH, DISP_HEIGHT])

done = False
clock = pygame.time.Clock()


class Room:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dir = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    random.shuffle(self.dir)

  def get_cur_pos(self):
    return self.x, self.y

  def get_next_pos(self):
    return self.dir.pop()

def make_maze(size, sw, sh, ew, eh):
  rooms = [[Room(x, y) for x in range(size)] for y in range(size)]
  maze = [[1 for _ in range(size*2+1)] for _ in range(size*2+1)]

  visited = []

  def make(cur_room, sw, sh, ew, eh):
    cx, cy = cur_room.get_cur_pos()
    # if (cx == ew) and (cy == eh): return
    
    visited.append((cx, cy))
    maze[cy*2+1][cx*2+1] = 0
    while cur_room.dir:
      nx, ny = cur_room.get_next_pos()
      if 0 <= nx < size and 0 <= ny < size:
        if (nx, ny) not in visited:
          maze[cy+ny+1][cx+nx+1] = 0
          make(rooms[ny][nx], sw, sh, ew, eh)

  make(rooms[sw][sh], sw, sh, ew, eh)

  return maze


def Input_Data():
  readl = sys.stdin.readline
  size = int(input('input map size(N*N) -> size: '))
  W, H = size*2, size*2
  sw, sh, ew, eh = map(int, input('input start(y, x) and end(y, x) -> sy sx ey ex: ').split())
  # map_maze = [[1] + list(map(int, readl().strip())) + [1] if 1<=h<=H else [1] * (W+2) for h in range(H+2)]
  # map_maze = [[1] + list(np.random.randint(0, 2, size=(W))) + [1] if 1<=h<=H else [1]*(W+2) for h in range(H+2)]
  map_maze = make_maze(size, sw, sh, ew, eh)
  return W, H, sw, sh, ew, eh, map_maze 
  


def Bfs(sw:int, sh:int, ew:int, eh:int, map_maze:list) -> int:
  global clock
  global done
  direct = ((0, -1), (0, 1), (-1, 0), (1, 0))
  q = deque()

  q.append((sw, sh, 0))
  map_maze[sh][sw] = 1

  while q:
    w, h, cost = q.popleft()
    # print(h, w, cost)
    pygame.draw.rect(screen, blue, pygame.Rect(w*CELL_SIZE, h*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for dw, dh in direct:
      nw, nh, ncost = w+dw, h+dh, cost+1
      if (not 0<nw<=W) or (not 0<nh<=H) or map_maze[nh][nw] != 0:
        continue
      
      if nw==ew and nh==eh:
        pygame.draw.rect(screen, red, pygame.Rect(nw*CELL_SIZE, nh*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        clock.tick(speed)

        while not done:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              done = True
            
        # return ncost
  
      q.append((nw, nh, ncost))
      map_maze[nh][nw] = 1
      
      pygame.display.update()
      clock.tick(speed)
  # return -1


def Dfs(w:int, h:int, ew:int, eh:int, cost:int, map_maze:int, res:list):
  global done
  global clock
  direct = ((0, -1), (0, 1), (-1, 0), (1, 0))
  map_maze[h][w] = 1
  # print("(%d, %d) %d"%(h, w, cost))
  if (h==eh) and (w==ew):
    # print('d', cost, res[0])
    res[0] = cost if res[0] > cost else res[0]
    pygame.draw.rect(screen, red, pygame.Rect(w*CELL_SIZE, h*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    clock.tick(speed)
    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
    return

  pygame.draw.rect(screen, blue, pygame.Rect(w*CELL_SIZE, h*CELL_SIZE, CELL_SIZE, CELL_SIZE))
  pygame.display.update()
  clock.tick(speed)
  
  for dw, dh in direct:
    nw, nh = w+dw, h+dh

    if 0<nw<=W and 0<nh<=H and map_maze[nh][nw] != 1:
      Dfs(nw, nh, ew, eh, cost+1, map_maze, res)
      pygame.draw.rect(screen, black, pygame.Rect(nw*CELL_SIZE, nh*CELL_SIZE, CELL_SIZE, CELL_SIZE))
      pygame.display.update()
      clock.tick(speed)
      map_maze[nh][nw] = 0


def drawMaze(sw, sh, ew, eh):
  for y in range(0, len(map_data)):
    for x in range(0, len(map_data[0])):
      # print(f'({x}, {y})')
      x_start, y_start = x*CELL_SIZE, y*CELL_SIZE
      if map_data[y][x] == 1:
        pygame.draw.rect(screen, gray, pygame.Rect(x_start, y_start, CELL_SIZE, CELL_SIZE))
      else:
        pygame.draw.rect(screen, black, pygame.Rect(x_start, y_start, CELL_SIZE, CELL_SIZE))

  pygame.draw.rect(screen, yellow, pygame.Rect(sw*CELL_SIZE, sh*CELL_SIZE, CELL_SIZE, CELL_SIZE))
  pygame.draw.rect(screen, blue, pygame.Rect(ew*CELL_SIZE, eh*CELL_SIZE, CELL_SIZE, CELL_SIZE))

  for x in range(0, (len(map_data[0])+1)*CELL_SIZE, CELL_SIZE):
    pygame.draw.line(screen, black, (x, 0), (x, len(map_data)*CELL_SIZE))
  for y in range(0, (len(map_data)+1)*CELL_SIZE, CELL_SIZE):
    pygame.draw.line(screen, black, (0, y), (len(map_data[0])*CELL_SIZE, y))

  pygame.display.update()
  clock.tick(speed)

def runGame():
  global done
  screen.fill(white)
  drawMaze(sw*2+1, sh*2+1, ew*2+1, eh*2+1)

  pygame.time.delay(2000) # wait 2 sec to start
  
  # Bfs(sw*2+1, sh*2+1, ew*2+1, eh*2+1, map_data)
  res = [99999999999999999999]
  Dfs(sw*2+1, sh*2+1, ew*2+1, eh*2+1, 0, map_data, res)
 
W, H, sw, sh, ew, eh, map_data = Input_Data()
runGame()
pygame.quit()
