# https://www.acmicpc.net/problem/14620
import sys, itertools
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
leaf = ((-1, 0), (1, 0), (0, -1), (0, 1))
cost = []
for i in range(1, N - 1):
    for j in range(1, N - 1):
        cost.append((arr[i][j] + sum([arr[i + x][j + y] for x, y in leaf]), i, j))
result = []
for f1, f2, f3 in list(itertools.combinations(range((N-2)**2), 3)):
    total_cost = 0
    discoverd = set()
    for c, i, j in [cost[f1], cost[f2], cost[f3]]:
        discoverd.add((i, j))
        total_cost+=c
        for li, lj in leaf:
            discoverd.add((li+i,lj+j))
    if len(discoverd) == 15:
        result.append(total_cost)
print(min(result))