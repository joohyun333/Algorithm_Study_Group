import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if maze[i][j] == '1' and not visited[i][j]:
                queue.append((i,j))
                while queue:
                    y, x = queue.popleft()
                    if y == N-1 and x == M-1:
                        return visited[y][x] + 1
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == '1':
                            if not visited[ny][nx]:
                                queue.append((ny,nx))
                                visited[ny][nx] = visited[y][x] + 1

N, M = map(int, input().split())
maze = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
print(bfs())