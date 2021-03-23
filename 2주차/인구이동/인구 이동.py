import sys, collections
input= sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0
while True:
    new_arr= [[0]*N for _ in range(N)]
    discoverd = [[False]*N for _ in range(N)]
    union = collections.defaultdict(list)
    count = 0
    for i in range(N):
        for j in range(N):
            if not discoverd[i][j]:
                count+=1
                discoverd[i][j] = True
                queue = collections.deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    union[count].append((x,y))
                    for ax, by in [(a+x,b+y) for a, b in direction if 0<=a+x<N and 0<=b+y<N and L<=abs(arr[x][y]-arr[a+x][b+y])<=R]:
                        if not discoverd[ax][by]:
                            discoverd[ax][by] = True
                            queue.append((ax, by))
    for i in union:
        total = 0
        for jx, jy in union[i]:
            total += arr[jx][jy]
        total = total//len(union[i])

        for jx, jy in union[i]:
            new_arr[jx][jy] = total
    if arr == new_arr:
        print(result)
        break
    else:
        result+=1
        arr = new_arr
