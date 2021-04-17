n, c = map(int, input().split())
house = []
for _ in range(n):
  house.append(int(input()))

start = 1
end = house[-1] - house[0]

def solution(start, end):
  answer = 0
  
  while start <= end:
    mid = (start + end) // 2
    router = 1
    pre = house[0] 
    
    for i in range(1, n):
      if pre + mid <= house[i]:
        pre = house[i]
        router += 1
    if router >= c:
      start = mid + 1
      answer = mid
    else:
      end = mid -1

  return answer

print(solution(start, end))
