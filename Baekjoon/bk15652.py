# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# 예제 입력 3 
# 3 3
# 예제 출력 3 
# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 2
# 1 2 3
# 1 3 3
# 2 2 2
# 2 2 3
# 2 3 3
# 3 3 3
from sys import stdin
from itertools import product


def Input_Data():
    readl = stdin.readline
    N, M = map(int, readl().split(' '))

    return N, M


def combination():
    res = []
    nums = [num for num in range(1, N+1)]
    res = list(product(nums, repeat=M))
    return res
    


N, M = Input_Data()
res = combination()
for i in res:
    print(*i)