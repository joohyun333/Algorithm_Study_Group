
def search(mid):
    conv = 0
    max_len = len(board)-1
    # mid 만큼 휴개소 갯수 탐색
    for i in range(max_len):
        conv += (board[i+1] - board[i]-1)//mid
    return conv

n = int(input())
board = list(map(int, input().split()))
board.sort()

left, right = 0, n-1
max_mix = float('inf')

while left < right:
    mix = board[left] + board[right]

    if abs(mix) <= max_mix:
        save = [left, right]
        max_mix = abs(mix)

        if mix==0:
            break
    if mix < 0:
        left += 1

    else:
        right -= 1


print(board[save[0]], board[save[1]])
