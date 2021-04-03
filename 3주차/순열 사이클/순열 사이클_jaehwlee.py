def dfs(x):
  visited[x] = True
  next_n = num_list[x]
  if not visited[next_n]:
    dfs(next_n)
   
  
t = int(input())

for _ in range(t):
  n = int(input())
  num_list = [0] + list(map(int, input().split()))
  visited = [True] + [False] * n
  cycle = 0
  
  for i in range(1, n+1):
    if not visited[i]:
      dfs(i)
      cycle += 1
      
  print(cycle)
