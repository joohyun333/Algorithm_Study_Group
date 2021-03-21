N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
# 치킨집 찾기
def find(idx, x, y):
    global ans
    if(idx == M):
        r = []
        for i in range(N):
            for j in range(N):
                if(data[i][j] == 3):
                    r.append((i,j))
        res = far(r, house)
        if(ans > sum(res)):
            ans = sum(res)
        return
    else:
        for i in range(x, N):
            if(i == x):
                k = y
            else:
                k = 0
            for j in range(k, N):
                if(data[i][j] == 2):
                    data[i][j] = 3
                    find(idx+1, i, j+1)
                    data[i][j] = 2


# 도시의 치킨거리 구해주기
def far(c, h):
    res = []
    for i in h:
        minV = 999999
        for j in c:
            dist = abs(i[0]-j[0]) + abs(i[1]-j[1])
            minV = min(minV, dist)
        res.append(minV)
    return res

ans = 999999
# 집, 치킨집 개수
chicken = 0
house = []
for i in range(N):
    for j in range(N):
        if(data[i][j] == 1):
            house.append((i,j))
        elif(data[i][j] == 2):
            chicken += 1

find(0,0,0)
print(ans)
