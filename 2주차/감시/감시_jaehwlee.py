# 너무 오래걸렸다
from copy import deepcopy
from collections import deque
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
cctv_map = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9


def up(x, y, cctv_map):
  for i in range(x-1, -1, -1):
    if cctv_map[i][y] == 0:
      cctv_map[i][y] = -1
    elif cctv_map[i][y] == 6:
      break
    

def down(x, y, cctv_map):
  for i in range(x + 1, n):
    if cctv_map[i][y] == 0:
      cctv_map[i][y] = -1
    elif cctv_map[i][y] == 6:
      break
    
    
def left(x, y, cctv_map):
  for i in range(y-1, -1, -1):
    if cctv_map[x][i] == 0:
      cctv_map[x][i] = -1
    elif cctv_map[x][i] == 6:
      break

    
def right(x, y, cctv_map):
  for i in range(y, m):
    if cctv_map[x][i] == 0:
      cctv_map[x][i] = -1
    elif cctv_map[x][i] == 6:
      break

    

def find_cctv():
  pos = deque()
  for i in range(n):
    for j in range(m):
      if 0 < cctv_map[i][j] < 6:
        pos.append([i, j, cctv_map[i][j]])
  return pos


q = find_cctv()


def dfs(cctv_num):
  global cctv_map
  global answer
    
  # 모든 cctv를 다 검사했으면 answer값 업데이트  
  if cctv_num == len(q):
    result = 0
    for i in range(n):
      for j in range(m):
        if cctv_map[i][j] == 0:
          result += 1
    answer = min(result, answer)
  
  else:
    # cctv 종류마다 노가다
    x, y, num = q[cctv_num]
    tmp_arr = deepcopy(cctv_map)
    if num == 1:
      up(x, y, cctv_map)
      dfs(cctv_num+1)

      cctv_map = deepcopy(tmp_arr)
      down(x, y, cctv_map)
      dfs(cctv_num+1)

      cctv_map = deepcopy(tmp_arr)
      left(x, y, cctv_map)
      dfs(cctv_num+1)

      cctv_map = deepcopy(tmp_arr)
      right(x, y, cctv_map)
      dfs(cctv_num+1)
    
    elif num == 2:
      # 상 하 
      up(x, y, cctv_map)
      down(x, y, cctv_map)
      dfs(cctv_num+1)

      # 좌 우
      cctv_map = deepcopy(tmp_arr)
      left(x, y, cctv_map)
      right(x, y, cctv_map)
      dfs(cctv_num+1)

    elif num == 3:
      # 상 우
      up(x, y, cctv_map)
      right(x, y, cctv_map)
      dfs(cctv_num+1)

      # 상 좌
      cctv_map = deepcopy(tmp_arr)
      up(x, y, cctv_map)
      left(x, y, cctv_map)
      dfs(cctv_num+1)

      # 우 하 
      cctv_map = deepcopy(tmp_arr)
      right(x, y, cctv_map)
      down(x, y, cctv_map)
      dfs(cctv_num+1)

      # 좌 하
      cctv_map = deepcopy(tmp_arr)
      left(x, y, cctv_map)
      down(x, y, cctv_map)
      dfs(cctv_num+1)

    elif num == 4:
      # 상 하 우 
      up(x, y, cctv_map)
      down(x, y, cctv_map)
      right(x, y, cctv_map)
      dfs(cctv_num+1)

      # 상 하 좌 
      cctv_map = deepcopy(tmp_arr)
      up(x, y, cctv_map)
      down(x, y, cctv_map)
      left(x, y, cctv_map)
      dfs(cctv_num+1)

      # 좌 우 상
      cctv_map = deepcopy(tmp_arr)
      left(x, y, cctv_map)
      right(x, y, cctv_map)
      up(x, y, cctv_map)
      dfs(cctv_num+1)

      # 좌 우 하
      cctv_map = deepcopy(tmp_arr)
      left(x, y, cctv_map)
      right(x, y, cctv_map)
      down(x, y, cctv_map)
      dfs(cctv_num+1)
    
    else:
      cctv_map = deepcopy(tmp_arr)
      up(x, y, cctv_map)
      left(x, y, cctv_map)
      right(x, y, cctv_map)
      down(x, y, cctv_map)
      dfs(cctv_num+1)


dfs(0)
print(answer)
