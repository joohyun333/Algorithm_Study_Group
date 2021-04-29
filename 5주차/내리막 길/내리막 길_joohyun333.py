# https://www.acmicpc.net/problem/1520
import sys

input = sys.stdin.readline
m, n = map(int, input().split())
h = []
ht = []
path = [[0] * n for i in range(m)]
path[0][0] = 1
for i in range(m):
    h.append([*map(int, input().split())])
    for j in range(n):
        ht.append((h[i][j], i, j))
ht.sort(reverse=True)
print(ht)
for (x, i, j) in ht:
    for (i1, j1) in filter(lambda t: t[0] in range(m) and t[1] in range(n),[(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]):
        if h[i1][j1] > x:
            path[i][j] += path[i1][j1]
print(path[m - 1][n - 1])