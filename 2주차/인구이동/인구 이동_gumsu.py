from collections import deque
import copy

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def BFS(x, y):
    migration = set() # 중복 방지
    q = deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()
        for k in range(4):
            xx = a + dx[k]
            yy = b + dy[k]
            # 방문 안했고, 범위 안에 존재할 때
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and l <= abs(arr[xx][yy] - arr[a][b]) <= r:
                visited[a][b] = True
                visited[xx][yy] = True
                q.append((xx, yy))
                migration.add((a, b))
                migration.add((xx, yy))
    return migration

while True:
    visited = [[False]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                country = BFS(i, j)
            if country:
                flag = True
                people = int(sum(arr[a][b] for a, b in country) / len(country))
                for w, v in country:
                    arr[w][v] = people

    if not flag:
        break
    cnt += 1
print(cnt)
# for z in arr:
#     print(z)