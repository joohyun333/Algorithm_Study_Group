# python으로 하면 시간초과, pypy로 해야 통과
n = int(input())
pipe_map = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y, d):
  global answer
  if x == n-1 and y == n-1:
    answer += 1
    return
   
  # 오른쪽이나 대각선으로 움직였으면 
  if d == 'right' or d == 'diag':
    if y + 1 < n and pipe_map[x][y+1] == 0:
      dfs(x, y+1, 'right')
    
  # 아래쪽
  if d == 'down' or d == 'diag':
    if x + 1 < n and pipe_map[x+1][y] == 0:
      dfs(x+1, y, 'down')
    
  # 대각선
  if x + 1 < n and y + 1 < n and pipe_map[x+1][y] == 0 and pipe_map[x][y+1]==0 and pipe_map[x+1][y+1]==0:
    dfs(x+1, y+1, 'diag')

    
answer = 0
dfs(0, 1, 'right')
print(answer)
