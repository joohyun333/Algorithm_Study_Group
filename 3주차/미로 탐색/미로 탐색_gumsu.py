from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())

miro = [list(map(int, input())) for _ in range(n)]
distance = [[0]*m for _ in range(n)]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    distance[x][y] = 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1 :
                miro[nx][ny] = -1
                distance[nx][ny] = distance[a][b] + 1
                q.append((nx, ny))

BFS(0, 0)
print(distance[n-1][m-1])