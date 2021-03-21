def valid_check(i,j):
    for y, x in direction:
        if i+y < 0 or i+y > N-1 or i+x < 0 or i+y > N-1 or visited[i+y][j+x]:
            return False
    return True

def cal(i,j):
    result = 0
    for y, x in direction:
        result += cost[i+y][j+x]
    return result

# 시작할 위치, 꽃개수, 현재까지 더해진 가격
def dfs(si, cnt, tmp_cost):
    global minV
    if tmp_cost >= minV:
        return
    if cnt == 3:
        minV = min(minV, tmp_cost)
        return
    for i in range(si, N-1):
        for j in range(1, N-1):
            if valid_check(i,j):
                for y, x in direction:
                    visited[i+y][j+x] = 1
                dfs(i, cnt+1, tmp_cost+cal(i,j))
                for y, x in direction:
                    visited[i+y][j+x] = 0

N = int(input())
minV =  (N**2)*200
cost = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
direction = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
dfs(1,0,0)
print(minV)
