# 맞긴 했는데 5392ms 걸림
from collections import deque

n, m = map(int, input().split())
wall_map = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]


def bfs(x, y, state):
  q = deque()
  q.append([x, y, state])
  visited[x][y][state] = 1

  while q:
    now_x, now_y, now_state = q.popleft()
    if now_x == n-1 and now_y == m-1:
      return visited[now_x][now_y][now_state]
    for i in range(4):
      nx = now_x + dx[i]
      ny = now_y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][now_state]==0:
        # 다음 맵이 이동할 수 있는 곳일 때
        if wall_map[nx][ny]==0:          
          visited[nx][ny][now_state] = visited[now_x][now_y][now_state] + 1
          q.append((nx, ny, now_state))
        # 다음 맵이 벽인데 아직 벽을 안 부쉈을 때
        #elif now_state == 0:
        if wall_map[nx][ny]==1 and now_state == 0:
          visited[nx][ny][1] = visited[now_x][now_y][0] + 1
          q.append((nx, ny, 1))
  return -1

print(bfs(0,0,0))
