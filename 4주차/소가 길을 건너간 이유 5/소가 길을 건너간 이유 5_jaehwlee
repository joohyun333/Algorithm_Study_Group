# pypy로 해야 시간 초과가 안 난다

n, k, b = map(int, input().split())
broken = [False for _ in range(n+1)]

for _ in range(b):
  now = int(input())
  broken[now] = True
    
def solution(n, k, b):
  answer = 1e9
  for i in range(1, n-k+2):
    fix = 0
    for j in range(i, i+k):
      if broken[j]:
        fix += 1
    answer= min(answer, fix)
  return answer

print(solution(n, k, b))
