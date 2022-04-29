# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
# Input
# 5
# 2 4 -10 4 -9
# Output
# 2 3 0 3 1

from sys import stdin

def Input_Data():
    readl = stdin.readline
    N = int(readl())
    data = list(map(int, readl().split(' ')))
    return N, data


def Solve1(): # FAIL - timeout
    compress = list(set(coordinate))
    print(compress)
    compress.sort()
    print(compress)

    for c in coordinate:
        print(compress.index(c), end=' ')
    print()


def Solve2():
    compress = list(set(coordinate))
    compress.sort()
    # print('compress', compress)
    compDic = dict()
    for i, key in enumerate(compress):
        compDic[key] = i
        # print(compDic)

    for c in coordinate:
        print(compDic[c], end=' ')
    print()
    

N, coordinate = Input_Data()
# print(N, coordinate)
# Solve1()
Solve2()