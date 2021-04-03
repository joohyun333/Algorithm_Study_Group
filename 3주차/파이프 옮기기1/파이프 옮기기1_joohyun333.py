# https://www.acmicpc.net/problem/17070
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
DP[0][1] = [1, 0, 0]


def pipe(y, x):
    a, b, c = DP[y][x]
    if a > 0:
        if 0 <= y < N and 0 <= x + 1 < N and arr[y][x + 1] == 0:
            DP[y][x + 1][0] += a
        if 0 <= y + 1 < N and 0 <= x + 1 < N and (arr[y][x + 1] == 0 and arr[y+1][x + 1] == 0 and arr[y+1][x] == 0):
                DP[y + 1][x + 1][1] += a
    if b > 0:
        if 0 <= y < N and 0 <= x + 1 < N and arr[y][x + 1] == 0:
            DP[y][x + 1][0] += b
        if 0 <= y + 1 < N and 0 <= x + 1 < N and (arr[y][x + 1] == 0 and arr[y+1][x + 1] == 0 and arr[y+1][x] == 0):
            DP[y + 1][x + 1][1] += b
        if 0 <= y + 1 < N and 0 <= x < N and arr[y+1][x] == 0:
            DP[y + 1][x][2] += b
    if c > 0:
        if 0 <= y + 1 < N and 0 <= x + 1 < N and (arr[y][x + 1] == 0 and arr[y+1][x + 1] == 0 and arr[y+1][x] == 0):
            DP[y + 1][x + 1][1] += c
        if 0 <= y + 1 < N and 0 <= x < N and arr[y+1][x] == 0:
            DP[y + 1][x][2] += c


for i in range(N):
    for j in range(N):
        pipe(i, j)

print(sum(DP[N-1][N-1]))
