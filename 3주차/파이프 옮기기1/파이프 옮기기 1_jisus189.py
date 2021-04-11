def dfs(x, y, shape):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return
    if board[n-1][n-1]==1:
        return

    if shape != 1:
        if y + 1 < n:
            if board[x][y+1] == 0:
                dfs(x, y+1, 0)
    if shape != 0:
        if x + 1 < n:
            if board[x+1][y] == 0:
                dfs(x+1, y, 1)

    if x + 1 < n and y + 1 < n:
        if board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, 1, 0)
print(ans)