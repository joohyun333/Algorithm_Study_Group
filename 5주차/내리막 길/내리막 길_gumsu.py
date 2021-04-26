m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1]*n for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 처음 방문한 정점이라면 0으로 초기화
    dp[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] < board[x][y]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))

# for z in dp:
#     print(z)