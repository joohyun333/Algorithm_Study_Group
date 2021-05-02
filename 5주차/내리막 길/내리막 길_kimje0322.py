import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(y,x):
    if dp[y][x] != -1:
        return dp[y][x]
    tmp = 0
    for r, c in directions:
        ny, nx = y+r, x+c
        if 0 <= ny < N and 0 <= nx < M and road[y][x] > road[ny][nx]:
            dp[y][x] += dfs(ny,nx)
            tmp += dfs(ny,nx)
    dp[y][x] = tmp
    return dp[y][x]
# 세로, 가로
N, M = map(int, input().split())
directions = [(-1,0),(1,0),(0,-1),(0,1)]
road = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
dp[N-1][M-1] = 1
print(dfs(0,0))
