
n, c = map(int, input().split())
board = []

for i in range(n):
    board.append(int(input()))

board.sort()

left, right = 1, board[-1]-board[0]

ans = 0

while left <= right:
    mid = (left+right) // 2
    start = board[0]
    cnt = 1
    # 공유기 개수 세면서 이동
    for i in range(1,len(board)):
        if board[i] >= start+mid:
            cnt+=1
            start = board[i]
    if cnt >= c:
        left = mid +1
        ans = mid
    else:
        right = mid -1


print(ans)
