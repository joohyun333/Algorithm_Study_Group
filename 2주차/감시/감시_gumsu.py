import copy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
camera = [] # 카메라 숫자, 좌표
board = [[0]*m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        board[i][j] = tmp[j]
        # 0 빈칸 1~5 cctv 6 벽
        if 0 < board[i][j] < 6:
            camera.append((board[i][j],i,j))

blind_spot = 64 # 사각 지대
camera_size = len(camera) # 카메라 사이즈 따로 저장

def DFS(level, dir):
    # print(dir)
    global blind_spot
    if level == camera_size:
        new_board = copy.deepcopy(board)
        cnt = 0
        for i in range(camera_size):
            cctv(camera[i][1], camera[i][2], camera[i][0], new_board, dir[i])
        for i in range(n):
            for j in range(m):
                if new_board[i][j] == 0:
                    cnt += 1
        blind_spot = min(blind_spot, cnt)
    else:
        for i in range(4):
            dir[level] = i
            DFS(level + 1, dir)

# 한 쪽 면만 보는 모니터
def monitor(x, y, dir, new_board):
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= n or y < 0 or y >=m or new_board[x][y] == 6:
            break
        if new_board[x][y] == 0:
            new_board[x][y] = -1

def cctv(x, y, camera_number, new_board, dir):
    if camera_number == 1:
        monitor(x, y, dir, new_board)
    elif camera_number == 2:
        monitor(x, y, dir, new_board)
        monitor(x, y, (dir + 2) % 4, new_board)
    elif camera_number == 3:
        monitor(x, y, dir, new_board)
        monitor(x, y, (dir + 1) % 4, new_board)
    elif camera_number == 4:
        monitor(x, y, dir, new_board)
        monitor(x, y, (dir + 1) % 4, new_board)
        monitor(x, y, (dir + 3) % 4, new_board)
    else:
        monitor(x, y, dir, new_board)
        monitor(x, y, (dir + 1) % 4, new_board)
        monitor(x, y, (dir + 2) % 4, new_board)
        monitor(x, y, (dir + 3) % 4, new_board)

DFS(0, [0]*camera_size)

# for z in board:
#     print(z)
# print(camera)
print(blind_spot)