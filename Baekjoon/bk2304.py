from sys import stdin


def Input_Data():
	readl = stdin.readline
	N = int(readl())
	H = [list(map(int, readl().split())) for _ in range(N)]
	
	return N, H

def Find_Highest():
	highest = [0, 0]
	res = 0
	for i, h in enumerate(H):
		if h[1] > highest[1]:
			highest = h
			res = i
	
	return res, highest[1]


def Calc_Volume(height, direct):
	volume = 0
	stack = []
	if direct == 0:
		# print('l', height)
		stack.append(height[0])
		for pos, h in height[1:]:
			if stack[-1][1] > h: continue
			else:
				volume += (pos - stack[-1][0]) * stack[-1][1]
				# print(volume)
				stack.pop()
				stack.append((pos, h))
			
	else:
		# print('r', height)
		stack.append(height[-1])
		for pos, h in height[-2::-1]:
			if stack[-1][1] > h: continue
			else:
				volume += (stack[-1][0] - pos) * stack[-1][1]
				# print(volume)
				stack.pop()
				stack.append((pos, h))
			
			
		

	return volume

def Solve():
	res = 0
	H.sort()
	max_idx, res = Find_Highest()
	h_left = H[:max_idx+1]
	res += Calc_Volume(h_left, 0)
	h_right = H[max_idx:]
	res += Calc_Volume(h_right, 1)

	return res

N, H = Input_Data()

print(Solve())


