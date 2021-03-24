# https://www.acmicpc.net/problem/5212
import collections, copy, sys

N, C = map(int, input().split())
land = collections.deque()
arr = [["."] * (C + 2)]
for i in range(1,N+1):
    a = "." + input() + "."
    for j, e in enumerate(a):
        if e == "X":
            land.append((i, j))
    arr.append(list(a))
arr.append(["."] * (C + 2))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
after_50_years = copy.deepcopy(arr)

new_land = []
for y, x in land:
    a = [(y + i, x + j) for i, j in direction if 0 <= y + i < N + 2 and 0 <= x + j < C + 2 and arr[y + i][x + j] == "."]
    if len(a) >= 3:
        after_50_years[y][x] = "."
    else:
        new_land.append((y, x))

land.clear()
arr.clear()
direction.clear()

result = []
min_y, min_x, max_y, max_x = sys.maxsize,sys.maxsize,-sys.maxsize,-sys.maxsize
for i, j in new_land:
    if i > max_y: max_y = i
    if i < min_y: min_y = i
    if j > max_x: max_x = j
    if j < min_x: min_x = j

for i in [i[min_x:max_x+1] for i in after_50_years[min_y: max_y+1]]:
    print(''.join(i))