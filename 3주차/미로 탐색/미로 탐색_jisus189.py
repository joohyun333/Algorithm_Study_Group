import sys
from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution():
    global n, m, board, visited

    q = deque()

    q.append(0)

    result = 1

    while True:
        q_len = len(q)
        for i in range(q_len):
            nq = q.popleft()
            r = nq // 100
            c = nq % 100

            if r == n - 1 and c == m - 1:
                print(result)
                return

            for d in direction:
                nr = r + d[0]
                nc = c + d[1]

                if 0 <= nr < n and 0 <= nc < m:

                    if board[nr][nc] == 0: continue
                    if visited[nr][nc] == 1: continue

                    visited[nr][nc] += 1
                    q.append(nr * 100 + nc)
        result += 1


n, m = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

visited[0][0] += 1

solution()
