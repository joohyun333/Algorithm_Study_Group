
def search(mid):
    conv = 0
    max_len = len(board)-1
    # mid 만큼 휴개소 갯수 탐색
    for i in range(max_len):
        conv += (board[i+1] - board[i]-1)//mid
    return conv

n, m, l = map(int, input().split())
board = list(map(int, input().split()))

left, right = 0, l

board += [left, right]

board.sort()


while left <= right:
    mid = (left+right) // 2

    if search(mid) > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)
