T = int(input())
for _ in range(T):
  n = int(input())
  sticker = []
  for _ in range(2):
    tmp = list(map(int, input().split()))
    sticker.append(tmp)
    
  # 1열은 하나 전 대각선으로부터 온 값만
  sticker[0][1] += sticker[1][0]
  sticker[1][1] += sticker[0][0]

  for i in range(2, n):
  # 2열부터는 하나 전 대각선이나 둘 전 대각선으로부터 온 값 중 큰 거
    sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
    sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

  answer = max(sticker[0][n-1], sticker[1][n-1])
  print(answer)
  
