from copy import deepcopy

chess_map = [list(input().split()) for _ in range(8)]

from collections import deque

d = [(0,0) , (0, 1), (0, -1), (1,0), (-1, 0), (1,1), (1, -1), (-1, 1), (-1, -1)]

def bfs(x, y):
  q = deque()
  q.append([x, y])
  while q:
    visited = [[False]*8 for _ in range(8)]
    
    for _ in range(len(q)):
      now_x, now_y = q.popleft()

      if now_x == 0 and now_y == 7:
        return 1
      
      if chess_map2[now_x][now_y] == '#':
        continue
      
      for dx, dy in d:
        nx = now_x + dx
        ny = now_y + dy

        if 0 <= nx < 8 and 0 <= ny < 8 and chess_map2[nx][ny] == '.' and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append([nx, ny])

    chess_map2.pop()
    chess_map2.insert(0, list('.' * 8))
    
  return 0
          
print(bfs(7, 0))
  
