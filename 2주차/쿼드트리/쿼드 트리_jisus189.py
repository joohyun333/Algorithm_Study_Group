import sys

def solution(x, y, size):
    global board, n, answer
    chk = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if i < n and j < n:
                # print(i,j,board[i][j])
                if chk != board[i][j]:
                    answer += "("
                    for k in range(0, 2):
                        for l in range(0, 2):
                            solution(int(x + size / 2 * k), int(y + size / 2 * l), int(size / 2))
                    answer += ")"
                    return
            else:
                continue

    answer += str(chk)
    return


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    answer = ""
    solution(0, 0, n)

    print(answer)
