r, c, t = map(int, input().split())
dust_map = [list(map(int, input().split())) for _ in range(r)]
tmp_dust_map = [[0] * c for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
air_clear = 0


# 미세먼지 확산하는 함수
def spread_dust(x, y):
  if dust_map[x][y] == -1:
    tmp_dust_map[x][y] = -1
    global air_clear
    air_clear = x
    return
    
  dust_value = dust_map[x][y] // 5
  cnt = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny < 0 or nx >= r or ny >= c or dust_map[nx][ny] == -1:
      continue
    
    else:
      cnt += 1
      tmp_dust_map[nx][ny] += dust_value
  
  tmp_dust_map[x][y] += dust_map[x][y] - dust_value * cnt

  
# 위쪽 반시계 방향 공기 청정
def clear_up_dust(x):
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]
  now = tmp_dust_map[x][1]
  tmp_dust_map[x][1] = 0
  i = 0
  nx = x
  ny = 1

  while i < 4:
    nx += dx[i]
    ny += dy[i]
    next = tmp_dust_map[nx][ny]
    tmp_dust_map[nx][ny] = now
    now = next
    # 방향 전환
    if nx + dx[i] < 0 or nx + dx[i] > x or ny + dy[i] < 0 or ny + dy[i] >= c:
      i += 1

# 아래쪽 시계 방향 공기 청정
def clear_down_dust(x):
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  now = tmp_dust_map[x][1]
  tmp_dust_map[x][1] = 0
  i = 0
  nx = x
  ny = 1

  while i < 4:
    nx += dx[i]
    ny += dy[i]
    next = tmp_dust_map[nx][ny]
    tmp_dust_map[nx][ny] = now
    now = next
    # 방향 전환
    if nx + dx[i] < 0 or nx + dx[i] > x or ny + dy[i] < 0 or ny + dy[i] >= c:
      i += 1
      
      
# t초 동안 각 좌표에 대해 확산 및 청정되는 미세먼지값 업데이트
for i in range(t):
  for i in range(r):
    for j in range(c):
      spread_dust(i, j)
  clear_up_dust(air_clear-1)
  clear_down_dust(air_clear)
  dust_map = tmp_dust_map
  tmp_dust_map = [[0] * c for _ in range(r)]

  
# 정답 출력
answer = 0
for i in range(r):
  for j in range(c):
    if dust_map[i][j] == -1:
      continue
    answer += dust_map[i][j]

print(answer)
