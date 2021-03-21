# https://www.acmicpc.net/problem/15686
import sys, itertools

input = sys.stdin.readline
N, M = map(int, input().split())
house = []
chicken = []
for i in range(N):
    for j, e in enumerate(list(map(int, input().split()))):
        if e == 1:
            house.append([i, j])
        elif e == 2:
            chicken.append([i, j])

house_len, chicken_len = len(house), len(chicken)
house_dis = [[0] * chicken_len for _ in range(house_len)]
for i, h in enumerate(house):
    for j, c in enumerate(chicken):
        house_dis[i][j] = abs(h[0] - c[0]) + abs(h[1] - c[1])

left_chicken = list(itertools.combinations(range(chicken_len),M))
result = sys.maxsize
for i in left_chicken:
    total = 0
    for j in house_dis:
        total += min(j[i_i] for i_i in i)
    if total < result:
        result = total
print(result)