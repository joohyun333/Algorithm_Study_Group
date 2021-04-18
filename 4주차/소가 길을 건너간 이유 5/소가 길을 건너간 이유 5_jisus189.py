

n, k, b = map(int, input().split())
board = []
sign = [False for i in range(n+1)]

for i in range(b):
    temp = int(input())
    sign[temp] = True
    board.append(temp)

board.sort()

min_fix = float('inf')

left = 1

while left + k <= n + 1:
    mid = left + k # 5
    cnt = 0

    for i in range(left,mid):
        if sign[i]:
            cnt +=1

    if cnt <= k and min_fix > cnt:
        min_fix = cnt

    left +=1

print(min_fix)
