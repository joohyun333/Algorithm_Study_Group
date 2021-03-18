dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
res = 214783647

def plant(x, y, flag):
    total = board[x][y]
    if flag:
        visited[x][y] = True
    else:
        visited[x][y] = False
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]

        if flag:
            visited[xx][yy] = True
        else:
            visited[xx][yy] = False
        total += board[xx][yy]
    return total

def check(x, y):
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if xx < 0 or xx >= n or yy < 0 or yy >= n or visited[xx][yy]:
            return False
    return True

def DFS(level, cost):
    global res
    if level == 3:
        res = min(res, cost)
        return
    for i in range(1, n-1):
        for j in range(1, n-1):
            if not visited[i][j] and check(i, j):    # 유효한 자리이고, 다 방문이 안됐으면 꽃 심기
                fee = plant(i, j, True) # 꽃 심고 칠하기
                # print('----------------------------')
                # for z in visited:
                #     print(z)
                # print('----------------------------')
                DFS(level+1, cost+fee)
                plant(i, j, False)

DFS(0,0)

# for z in board:
#     print(z)

print(res)