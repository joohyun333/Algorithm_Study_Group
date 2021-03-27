import sys
input = sys.stdin.readline

def divide(n, y, x):
    global ans
    zero, one = 0, 0
    for i in range(y, y + n):
        for j in range(x, x + n):
            if zero and one:
                break
            if board[i][j] == '0':
                zero = 1
            elif board[i][j] == '1':
                one = 1

    if zero != one:
        if zero:
            ans += '0'
        elif one:
            ans += '1'
    else:
        small_n = n // 2
        ans += '('
        divide(small_n, y, x)
        divide(small_n, y, x + small_n)
        divide(small_n, y + small_n, x)
        divide(small_n, y + small_n, x + small_n)
        ans += ')'

N = int(input())
board = [input() for _ in range(N)]
ans = ''
divide(N,0,0)
print(ans)