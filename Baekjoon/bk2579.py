from sys import stdin
import time

def Input_Data():
    readl = stdin.readline
    n = int(readl())
    s = [int(readl()) for _ in range(n)]
    return n, s


def Solve_DP():
    memo = [0]*300

    if N < 3:
        return sum(stairs)
    elif N == 3:
        return max(stairs[2]+stairs[0], stairs[2]+stairs[1])
    else:
        memo[0] = stairs[0]
        memo[1] = stairs[0]+stairs[1]
        memo[2] = max(stairs[2]+stairs[0], stairs[2]+stairs[1])

        for i in range(3, N):
            memo[i] = max(stairs[i]+memo[i-2], stairs[i]+stairs[i-1]+memo[i-3])

    print(memo[:N])
    return memo[N-1]


def Solve_DP1():
    memo = []

    if N < 3:
        return sum(stairs)
    elif N == 3:
        return max(stairs[2]+stairs[0], stairs[2]+stairs[1])
    else:
        memo.append(stairs[0])
        memo.append(stairs[0] + stairs[1])
        memo.append(max(stairs[2]+stairs[0], stairs[2]+stairs[1]))

    for idx in range(3, N):
        memo.append(max(stairs[idx]+memo[idx-2], stairs[idx]+stairs[idx-1]+memo[idx-3]))

    return memo[-1]

N, stairs = Input_Data()


start_t = time.time()
print(Solve_DP1())
print(time.time() - start_t)


start_t = time.time()
print(Solve_DP())
print(time.time() - start_t)