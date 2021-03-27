def spread_dust():
    spread = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                dust = int(board[i][j]//5)
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    # 확산된 먼지만 따로 저장 , 실제 보드에서 확산된 먼지만큼 제거
                    if 0 <= x < r and 0 <= y < c and board[x][y] != -1:
                        spread[x][y] += dust
                        board[i][j] -= dust

    # 따로 저장해둔 확산된 먼지를 기존 보드에 다시 추가
    for i in range(r):
        for j in range(c):
            board[i][j] += spread[i][j]

def cleaning_dust():
    # 윗 바람
    up_air = 0
    up_row = cleaner[0]
    up_col = 0
    while True:
        nx = up_row + dx[up_air]
        ny = up_col + dy[up_air]
        if nx == up_row and ny == 0:
            break
        if nx < 0 or nx >= cleaner[1] or ny < 0 or ny >= c:
            up_air = (up_air + 1) % 4
        else:
            if board[nx][ny] != 0:
                if up_row == cleaner[0] and up_col == 0:    # 공기 정화
                    board[nx][ny] = 0
                else:
                    board[up_row][up_col] = board[nx][ny]
                    board[nx][ny] = 0
            up_row = nx
            up_col = ny

    # 아랫 바람
    down_air = 2
    down_row = cleaner[1]
    down_col = 0
    while True:
        nx = down_row + dx[down_air]
        ny = down_col + dy[down_air]
        if nx == cleaner[1] and ny == 0:
            break
        if nx < cleaner[1] or nx >= r or ny < 0 or ny >= c:
            down_air = (down_air + 3) % 4
        else:
            if board[nx][ny] != 0:
                if down_row == cleaner[1] and down_col == 0:    # 공기 정화
                    board[nx][ny] = 0
                else:
                    board[down_row][down_col] = board[nx][ny]
                    board[nx][ny] = 0
            down_row = nx
            down_col = ny

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c, t = map(int, input().split())
board = [[0]*c for _ in range(r)]
cleaner = []
for i in range(r):
    tmp = list(map(int, input().split()))
    for j in range(c):
        board[i][j] = tmp[j]
        if board[i][j] == -1:   # 공기청정기 위치 찾기
            cleaner.append(i)   # y좌표는 무조건 0

for _ in range(t):
    spread_dust()
    cleaning_dust()

total = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == -1 or board[i][j] == 0:
            continue
        total += board[i][j]

print(total)
# for z in board:
#     print(z)