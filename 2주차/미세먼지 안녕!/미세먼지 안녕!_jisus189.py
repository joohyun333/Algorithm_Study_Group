import sys

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
up_air = [(-1, 0), (0, 1), (1, 0), (0, -1)]
down_air = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(t, board):
    global air, r, c

    for _ in range(t):
        # 1. 미세먼지 확산
        temp_board = [[0] * c for __ in range(r)]

        for i in range(r):
            for j in range(c):
                if board[i][j] >= 5:
                    temp = 0
                    for d in direction:
                        if 0 <= i + d[0] < r and 0 <= j + d[1] < c:
                            if board[i + d[0]][j + d[1]] == -1: continue
                            temp_board[i + d[0]][j + d[1]] += int(board[i][j] / 5)
                            temp += int(board[i][j] / 5)
                    temp_board[i][j] += board[i][j] - temp
                else:
                    temp_board[i][j] += board[i][j]

        # 2. 공기청정기 작동
        i = air[0][0] - 1
        j = air[0][1]
        d = 0
        # print(i,j,"->",i + up_air[d][0],j + up_air[d][1])
        while temp_board[i][j] != -1:

            if i + up_air[d][0] == air[0][0] and j + up_air[d][1] == 0:
                break
            if 0 <= i + up_air[d][0] < air[0][0] + 1 and 0 <= j + up_air[d][1] < c:
                temp_board[i][j] = temp_board[i + up_air[d][0]][j + up_air[d][1]]
                i = i + up_air[d][0]
                j = j + up_air[d][1]
            else:
                d += 1
        temp_board[i][j] = 0
        i = air[1][0] + 1
        j = air[1][1]
        d = 0
        while temp_board[i][j] != -1:
            if i + down_air[d][0] == air[1][0] and j + down_air[d][1] == 0:
                break
            if air[1][0] <= i + down_air[d][0] < r and 0 <= j + down_air[d][1] < c:
                temp_board[i][j] = temp_board[i + down_air[d][0]][j + down_air[d][1]]
                i = i + down_air[d][0]
                j = j + down_air[d][1]
            else:
                d += 1
        temp_board[i][j] = 0

        board = temp_board[:]

    return sum(sum(i) for i in board) + 2


if __name__ == "__main__":
    r, c, t = map(int, sys.stdin.readline().split())

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

    air = []

    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:
                air.append([i, j])

    print(solution(t, board))

