# 가로, 세로, 대각선
dx = [0, 1, 1]
dy = [1, 0, 1]
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
# x, y, 파이프(가로 0 세로 1 대각선 2)
# 0 -> 0, 2
# 1 -> 1, 2
# 2 -> 2 -> 0
# 2 -> 1 -> 2
def DFS(x, y, z):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return
    if x >= n or y >= n or house[x][y]:
        return
    if z == 0 or z == 1:
        if y +1 < n and house[x][y+1] == 0:
            DFS(x, y+1, 0)
    if z == 1 or z == 2:
        if x +1 < n and house[x+1][y] == 0:
            DFS(x+1, y, 2)
    if z == 0 or z == 1 or z == 2:
        if x +1 < n and y +1 < n and house[x+1][y+1] == house[x+1][y] == house[x][y+1] == 0:
            DFS(x+1, y+1, 1)
    
    return cnt

print(DFS(0, 1, 0))