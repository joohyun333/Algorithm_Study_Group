def solution(x, y, n):
  # n이 1이면 입력받은 이미지에서 픽셀값을 갖고 옴 
  if n == 1:
    return images[x][y]
  
  # 현재 호출할 픽셀의 길이
  p = n//2
  
  # 차례대로 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래로 나누어 재귀 호출
  part1 = solution(x, y, p)
  part2 = solution(x, y + p, p)
  part3 = solution(x + p, y, p)
  part4 = solution(x + p, y + p, p)

  # 모든 걸 1픽셀 단위로 나눈 후 다시 합쳐가면서 정답을 산출
  if part1 == part2 == part3 == part4 and len(part1) == 1:
    return part1
  
  # 결과 출력 부분
  return "(" + part1 + part2 + part3 + part4 + ")"


n = int(input())
images = [input() for _ in range(n)]
print(solution(0, 0, n))

