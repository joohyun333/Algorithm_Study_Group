import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    tmp = []
    tmp.append([i,j])
    while queue:
        x,y = queue.popleft()
        for r, c in direction:
            nx, ny = x + r, y + c
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(border[nx][ny] - border[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    tmp.append([nx,ny])
    return tmp

N, L, R = map(int, input().split())
border = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
cnt = 0
while True:
    visited = [[0]*N for _ in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                tmp = bfs(i,j)
                if len(tmp) >= 2:
                    move = True
                    num = sum(border[x][y] for x,y in tmp) // len(tmp)
                    for x,y in tmp:
                        border[x][y] = num
    if not move:
        break
    cnt += 1
print(cnt)