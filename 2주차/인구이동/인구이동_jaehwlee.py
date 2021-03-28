# dfs보다 bfs로 풀었어야 했다.
import sys
sys.setrecursionlimit(10000)

n, l, r = map(int, input().split())
country_map = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0 , 0]
dy = [0, 0, -1, 1]
cnt = 0

# 조건이 맞으면 경계선을 허무는 함수
def dfs(x, y):
   for i in range(4):
     nx = x + dx[i]
     ny = y + dy[i]

     if nx < 0 or ny < 0 or nx >= n or ny >= n:
       continue
        
     # 조건에 맞으면 경계선을 허뭄
     if not visited[nx][ny]:
       diff = abs(country_map[x][y] - country_map[nx][ny])
       if l <= diff <= r:
         visited[nx][ny] = True
         group.append([nx, ny])
         dfs(nx, ny)


while True:
  visited = [[False] * n for _ in range(n)]
  flag = False
  for i in range(n):
    for j in range(n):
      group = []
      if not visited[i][j]:
        dfs(i, j)
        # 그룹이 형성되면 맵을 업데이트함
        if len(group)> 1:
          flag = True
          group.append([i, j])
          visited[i][j] = True
          avg = sum([country_map[x][y] for x, y in group]) // len(group)
          for x, y in group:
            country_map[x][y] = avg
        
  if not flag:
    print(cnt)
    break

  cnt += 1
