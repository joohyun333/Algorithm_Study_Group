import sys
input = sys.stdin.readline
def connect(y,x,d):
    for direction in directions[d]:
        dy, dx = next[direction]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and not data[ny][nx]:
            if direction == 2:
                if not data[ny-1][nx] and not data[ny][nx-1]:
                    dp[ny][nx][direction] += dp[y][x][d]
            else:
                dp[ny][nx][direction] += dp[y][x][d]

directions = {0:[0,2], 1:[1,2], 2:[0,1,2]}
next = {0: [0,1], 1:[1,0], 2:[1,1]}
N = int(input())
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
data = [list(map(int, input().split())) for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        for d in range(3):
            if dp[i][j][d] and not data[i][j]:
                connect(i,j,d)
print(sum(dp[N-1][N-1]))


# def check(y,x,d):
#     for direction in directions[d]:
#         dy, dx = cos[direction]
#         ny, nx = y+dy, x+dx
# #       유효한 범위이고 빈칸이면
#         if 0 <= ny < N and 0 <= nx < N and not data[ny][nx]:
#             if direction != 2:
#                 dp[ny][nx][direction] += dp[y][x][d]
#             else:
#                 if not data[ny-1][nx] and not data[ny][nx-1]:
#                     dp[ny][nx][direction] += dp[y][x][d]
#
# # 0가로, 1세로, 2대각선
# directions = {0:[0,2], 1:[1,2], 2:[0,1,2]}
# cos = {0: [0,1], 1:[1,0], 2:[1,1]}
# N = int(input())
# dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
# data = [list(map(int, input().split())) for _ in range(N)]
# dp[0][1][0] = 1
#
# for y in range(N):
#     for x in range(N):
#         for d in range(3):
#             if dp[y][x][d] and not data[y][x]:
#                 check(y,x,d)
# print(sum(dp[N-1][N-1]))

# 문제점
# 1. 56번줄의 prev_x, prev_y가 알맞게 바뀌지 않는다.
# 문제 의도상 bfs에 가까울 것 같으나 dfs를 쓴다면
# stack 맨뒤에 있는 요소를 pop해서
# 1. 문제점 해결은 될 거라 생각했지만
# 여전히 다른 답이 나옴.
# visited 표시가 안되서 그런거 아닐까 예측해봄 << 이것도 아닌것 같음
# 왜냐하면 한가지 경로에서 겹칠 일이 없음
# 다른 풀이에서도 visited를 사용하지 않음
# import sys
# input = sys.stdin.readline
# from collections import deque
# N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# queue = []
# queue.append((0,1))
# dq = deque(queue)
# data[0][0], data[0][1] = 3, 3
# # 0가로, 1세로, 2대각선
# # direction = [(0,1),(1,0),(1,1)]
# dx, dy = [1,0,1],[0,1,1]
# prev_x, prev_y = 0,0
# cnt = 0
# print(data)
# while dq:
#     y,x = dq.popleft()
#     if y == N-1 and x == N-1:
#         cnt += 1
#     # 현재 파이프 방향 찾기
#     for d in range(3):
#         if (prev_y+dy[d], prev_x+dx[d]) == (y,x):
#             dir = d
#             break
#     # 가로
#     if dir == 0:
#         # 다음 노드 빈칸인지 확인
#         # 1 우측
#         if 0 <= x+1 < N and not data[y][x+1]:
#             dq.append((y,x+1))
#         # 2 우측하단
#         if 0 <= y+1 < N and 0 <= x+1 < N and not data[y][x+1] and not data[y+1][x] and not data[y+1][x+1]:
#             dq.append((y+1, x+1))
#     # 세로
#     elif dir == 1:
#     # 1 하단
#         if 0 <= y+1 < N and not data[y+1][x]:
#             dq.append((y+1,x))
#     # 2 우측하단
#         if 0 <= y+1 < N and 0 <= x+1 < N and not data[y+1][x+1] and not data[y][x+1] and not data[y+1][x]:
#             dq.append((y+1, x+1))
#     # 대각선
#     elif dir == 2:
#     # 1 우측
#         if 0 <= x+1 < N and not data[y][x+1]:
#             dq.append((y,x+1))
#     # 2 하단
#         if 0 <= y+1 < N and not data[y+1][x]:
#             dq.append((y+1,x))
#     # 3 우측하단
#         if 0 <= y+1 < N and 0 <= x+1 < N and not data[y+1][x+1] and not data[y][x+1] and not data[y+1][x]:
#             dq.append((y+1,x+1))
#     prev_y, prev_x = y, x
#
# # 이전노드와 현재노드가 어떤 모양인지 확인(가로, 세로, 대각선)
# # 각 모양별로 가능한 다음 노드 stack에 넣기
# # bfs
# print(cnt)