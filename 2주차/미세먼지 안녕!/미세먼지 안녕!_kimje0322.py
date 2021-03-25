# pypy3
import sys
input = sys.stdin.readline

# 공기청정기 위치
def find():
    global cleaner
    for i in range(R):
        if data[i][0] == -1:
            cleaner = i
            return
# 미세먼지 확산
def diffusion():
    tmp = [[0] * C for _ in range(R)]
    global cleaner
    for r in range(R):
        for c in range(C):
            if data[r][c] // 5 >= 1:
                val = data[r][c] // 5
                for dir in direction:
                    i, j = dir
                    if 0 <= r + i < R and 0 <= c + j < C and data[r + i][c + j] >= 0:
                        tmp[r + i][c + j] += val
                        data[r][c] -= val
    for i in range(R):
        for j in range(C):
            data[i][j] += tmp[i][j]
    return

# 공기청정기 작동
def cleaning():
    cleaner1 = cleaner
    cleaner2 = cleaner + 1
    # up 아랫줄
    # 하단우측
    right_bottom = data[cleaner1][C-1]
    for c in range(C-1,1,-1):
        data[cleaner1][c] = data[cleaner1][c-1]
    data[cleaner1][1] = 0

    # up 오른쪽줄
    # 상단우측
    right_top = data[0][C-1]
    for r in range(cleaner1-1):
        data[r][C-1] = data[r+1][C-1]
    data[cleaner1-1][C-1] = right_bottom

    # up 윗줄
    # 상단좌측
    left_top = data[0][0]
    for c in range(C-2):
        data[0][c] = data[0][c+1]
    data[0][C-2] = right_top

    # up 왼쪽줄
    for r in range(cleaner1-1,1,-1):
        data[r][0] = data[r-1][0]
    data[1][0] = left_top

    # down 윗줄
    # 상단우측
    right_top = data[cleaner2][C-1]
    for c in range(C-1,1,-1):
        data[cleaner2][c] = data[cleaner2][c-1]
    data[cleaner2][1] = 0
    # down 오른쪽줄
    # 하단우측
    right_bottom = data[R-1][C-1]
    for r in range(R-1,cleaner2+1,-1):
        data[r][C-1] = data[r-1][C-1]
    data[cleaner2+1][C-1] = right_top
    # down 아랫줄
    # 하단좌측
    left_bottom = data[R-1][0]
    for c in range(C-2):
        data[R-1][c] = data[R-1][c+1]
    data[R-1][C-2] = right_bottom
    # down 왼쪽줄
    for r in range(cleaner2+1,R-1):
        data[r][0] = data[r+1][0]
    data[R-2][0] = left_bottom

R, C, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
# 공기청정기 행(r) 아랫부분
cleaner = 0
# 미세먼지 존재 구간
dust = []
find()
for _ in range(T):
    diffusion()
    cleaning()
ans = 0
for r in range(R):
    ans += sum(data[r])
print(ans+2)
