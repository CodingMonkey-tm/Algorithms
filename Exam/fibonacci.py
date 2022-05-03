# Memoization

from sys import stdin


def InputData():
    readl = stdin.readline
    return int(readl())


def fibonacci(n):
    if n in myMemo:
        return myMemo[n]
    else:
        result.append(fibonacci(n - 1) + fibonacci(n - 2))
        myMemo[n] = result[-1]
        return result[-1]


myMemo = {1:1, 2:1}
result = []

N = InputData()
print("res:", fibonacci(N))
print("memo:", myMemo)
print("result:", result)
