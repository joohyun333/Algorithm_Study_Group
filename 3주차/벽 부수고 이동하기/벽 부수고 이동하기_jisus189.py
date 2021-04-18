import sys
from collections import deque

direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def solution():
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0] * 2 for i in range(m)] for i in range(n)]

    visited[0][0][1] = 1
    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif board[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])
        print("(",x,',',y,")")
        for i in range(n):
            for j in range(m):
                print(visited[i][j], end="")
            print("")
        print("")

    return -1


n, m = map(int, input().split())

board = [list(map(int, list(input().strip()))) for _ in range(n)]

print(solution())
