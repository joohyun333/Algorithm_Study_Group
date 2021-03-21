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

# def find(cur):
#     global tmp1, tmp2
#     minV = 999999999
#     y, x = cur
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == 2:
#                 if minV > abs(y-i) + abs(x-j):
#                     minV = abs(y-i) + abs(x-j)
#                     tmp1, tmp2 = i, j
#     chicken_distance.append((cur, (tmp1, tmp2), minV))
#     return
#
# def find_minV(idx):
#     if idx == N - M:
#         pass
#
#     # chicken_distance에 안들어간 치킨집 고려
#     # 가장 먼저 지우기
#     # chicken_distance리스트에서 반복문 돌리면서
#     # n-m개 선택했을때 거리의 치킨거리 최솟값
#
#     return
#
# N, M = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]
# # 집 위치 / 치킨집 위치 / 치킨 거리
# chicken_distance = []
# # bfs로 각 치킨거리 구하기
# # 최소 도시의 치킨 거리 => 재귀함수
# # idx > N - M: 조건 -> return
# chicken = 0
# house = []
# tmp1, tmp2 = 0,0
# blacklst = []
# for i in range(N):
#     for j in range(N):
#         if data[i][j] == 1:
#             cur = (i,j)
#             find(cur)
#         elif data[i][j] == 2:
#             chicken.append((i,j))
# for c in chicken:
#     for cd in chicken_distance:
#         if not c in cd:
#             blacklst.append(c)
#
# print(chicken_distance)
