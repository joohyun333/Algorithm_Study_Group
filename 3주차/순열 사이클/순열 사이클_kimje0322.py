import sys
input = sys.stdin.readline

# 재귀
def dfs(start):
    visited[start] = 1
    next_node = data[start]
    if not visited[next_node]:
        dfs(next_node)
    return

for _ in range(int(input())):
    N = int(input())
    data = [0]+list(map(int, input().split()))
    cnt = 0
    visited = [0]*(N+1)
    for idx in range(1, N+1):
        if not visited[idx]:
            dfs(idx)
            cnt += 1
    print(cnt)