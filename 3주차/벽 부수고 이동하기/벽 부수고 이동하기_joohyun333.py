# https://www.acmicpc.net/problem/2206
import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(input().strip()) for i in range(N)]
dis = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    route = [[[False,False] for _ in range(M)] for _ in range(N)]
    queue = collections.deque([(1, False, (0, 0))])
    route[0][0] = [True, True]
    while queue:
        cost, wall, spot = queue.popleft()
        if spot[0] == N-1 and spot[1] == M-1:
            return cost
        for n, m in [(spot[0] + i, spot[1] + j) for i, j in dis if 0 <= spot[0] + i < N and 0 <= spot[1] + j < M]:
            if maps[n][m] == "0" and not route[n][m][wall]:
                route[n][m][wall] = True
                queue.append((cost+1, wall, (n,m)))
            elif maps[n][m] == "1" and not wall and not route[n][m][1]:
                route[n][m][1] = True
                queue.append((cost+1, True, (n,m)))
    return -1
print(bfs())
