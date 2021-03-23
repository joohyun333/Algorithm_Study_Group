import sys

input = sys.stdin.readline
R, C, T = map(int, input().split())
arr = []
air_cleaner = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(R):
    a = list(map(int, input().split()))
    for j in range(C):
        if a[j] == -1:
            air_cleaner.append((i, j))
    arr.append(a)
air_cleaner.sort()


def dust_spread():
    rest = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                d = [(x + i, y + j) for x, y in direction if
                     0 <= x + i < R and 0 <= y + j < C and (x + i, y + j) not in air_cleaner]
                for zx, zy in d:
                    rest[zx][zy] += arr[i][j] // 5
                rest[i][j] += arr[i][j] - ((arr[i][j] // 5) * len(d))
    return rest


def work_up():
    x = air_cleaner[0][0]
    rest = [arr[x][C - 1], arr[0][C - 1], arr[0][0]]
    for i in range(C - 1, 0, -1): arr[x][i] = arr[x][i-1]
    for i in range(x): arr[i][C - 1] = arr[i+1][C - 1]
    for i in range(C - 2): arr[0][i] = arr[0][i + 1]
    for i in range(x, 0, -1): arr[i][0] = arr[i-1][0]
    arr[x - 1][C - 1] = rest[0]
    arr[0][C - 2] = rest[1]
    arr[1][0] = rest[2]
    arr[x][0] = 0


def work_down():
    x = air_cleaner[1][0]
    rest = [arr[x][C - 1], arr[R - 1][C - 1], arr[R - 1][0]]
    for i in range(C - 1, 0, -1): arr[x][i] = arr[x][i-1]
    for i in range(R - 1, x, -1): arr[i][C - 1] = arr[i-1][C - 1]
    for i in range(C - 2): arr[R - 1][i] = arr[R - 1][i + 1]
    for i in range(x, R - 2): arr[i][0] = arr[i + 1][0]
    arr[x + 1][C - 1] = rest[0]
    arr[R - 1][C - 2] = rest[1]
    arr[R - 2][0] = rest[2]
    arr[x][0] = 0


for _ in range(T):
    arr = dust_spread()
    work_up()
    work_down()
print(sum([arr[i][j] for i in range(R) for j in range(C)]))
