# # https://www.acmicpc.net/problem/16954
import sys
from collections import deque

input = sys.stdin.readline
chess_board = [list(input().strip()) for _ in range(8)]


def bfs():
    queue = deque([[7, 0]])
    direction = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

    while queue:
        discovered = [[False] * 8 for _ in range(8)]
        for _ in range(len(queue)):
            y, x = queue.popleft()

            if y == 0 and x == 7:
                return 1

            if chess_board[y][x] == ".":
                for i, j in direction:
                    if 0 <= y + i < 8 and 0 <= x + j < 8 and chess_board[y + i][x + j] == "." and not discovered[y + i][x + j]:
                        discovered[y + i][x + j] = True
                        queue.append([y + i, x + j])
        chess_board.pop()
        chess_board.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])
    return 0


print(bfs())
