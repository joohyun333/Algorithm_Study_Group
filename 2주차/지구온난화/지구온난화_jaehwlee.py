from copy import deepcopy
r, c = map(int, input().split())
now_map = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 그냥 할당해주니 같이 값이 바뀜
future_map = deepcopy(now_map)

# 조건을 만족하는 50년 후 미래의 지도 생성 
for x in range(r):
  for y in range(c):
    if now_map[x][y] == '.':
      continue
    num_sea = 0
    # 조건 : 한 좌표에 대해서 상하좌우에 바다가 3칸 이상이면 해당 좌표를 바다로 바꿔줌
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= r or ny < 0 or ny >= c:
        num_sea += 1
        continue
      elif now_map[nx][ny] == '.':
        num_sea += 1
    
    if num_sea >= 3:
      future_map[x][y] = '.'

      
# 시작행 구하기
def get_start_row():
    for i in range(r):
        if 'X' in future_map[i]:
            return i

          
# 마지막행 구하기
def get_end_row():
    for i in range(r-1, -1, -1):
        if 'X' in future_map[i]:
            return i

          
# 시작열 구하기
def get_start_col():
    for j in range(c):
        column_arr = []
        for i in range(r):
            column_arr.append(future_map[i][j])
        if 'X' in column_arr:
            return j
          
          
# 마지막열 구하기
def get_end_col():
    for j in range(c-1, -1, -1):
        column_arr = []
        for i in range(r):
            column_arr.append(future_map[i][j])
        if 'X' in column_arr:
            return j
        
start_row = get_start_row()
start_col = get_start_col()
end_row = get_end_row()
end_col = get_end_col()

for i in range(start_row, end_row+1):
  for j in range(start_col, end_col + 1):
    print(future_map[i][j], end='')
  print()
