# https://www.acmicpc.net/problem/2178
import sys
input = sys.stdin.readline
N, M  = map(int, input().split())
path = []
for i in range(N):
    path.append(*map(str, input().split()))
route = [[0] * M for i in range(N)]
route[0][0] = 1
queue = [(0,0)]
while queue:
    v_x, v_y = queue.pop(0)
    if v_x == N-1 and v_y == M-1:
        break
    for (i, j) in filter(lambda t: t[0] in range(N) and t[1] in range(M),[(v_x+ 1, v_y ), (v_x - 1, v_y ), (v_x, v_y  + 1), (v_x, v_y  - 1)]):
        if path[i][j] == '1' and route[i][j] == 0:
            route[i][j] = route[v_x][v_y]+1
            queue.append((i, j))
print(route[N-1][M-1])