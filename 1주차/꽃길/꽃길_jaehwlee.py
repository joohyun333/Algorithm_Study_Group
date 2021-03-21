import sys
input = sys.stdin.readline

n =int(input())
flower_bed = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
min_cost = 1e9

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def available(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[x][y] or visited[nx][ny]:
      return False
  
  return True


def get_cost(x, y):
  cost = flower_bed[x][y]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    cost += flower_bed[nx][ny]
  return cost


def visit(x, y, flag=False):
  visited[x][y] = flag
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    visited[nx][ny]= flag


def dfs(ps, tmp_cost, cnt):
  global min_cost
  
  if tmp_cost >= min_cost:
    return
  
  if cnt == 3:
    min_cost = min(min_cost, tmp_cost)
    return

  for i in range(ps, n-1):
    for j in range(1, n-1):
      if available(i, j):
        visit(i, j, flag=True)
        dfs(i, tmp_cost + get_cost(i, j), cnt+1)
        visit(i, j, flag=False)
        
dfs(1,0,0)
print(min_cost)
