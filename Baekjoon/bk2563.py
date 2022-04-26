from sys import stdin
import time


def Input_Data():
	readl = stdin.readline
	n = int(readl())
	papers = [list(map(int, readl().split(' ')))for _ in range(n)]
	
	return n, papers

def Solve(n, papers):
	# START_TIME = time.time()

	canvas = [[0 for _ in range(100)] for _ in range(100)]
	res = 0

	for i in range(n):
		x, y = map(int, papers[i])
		for h in range(y, y+10):
			for w in range(x, x+10):
				canvas[h][w] = 1

	for row in canvas:
		res += sum(row)

	# END_TIME = time.time()
	# print("time: ", END_TIME - START_TIME)

	return res

N, papers = Input_Data()
print(Solve(N, papers))