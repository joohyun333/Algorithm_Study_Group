import sys, collections, itertools

input = sys.stdin.readline
N, M = map(int, input().split())
arr = collections.defaultdict(list)
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M):
        if a[j] > 0:
            arr[a[j]].append((i, j))

combin = [[(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],
          [(1, 0, 1, 0), (0, 1, 0, 1)],
          [(1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1)],
          [(1, 1, 1, 0), (0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1)],
          [(1, 1, 1, 1)]]


def camera(p, c):
    y, x = p[0], p[1]
    n, w, s, e = c[0], c[1], c[2], c[3] # 12시 , 9시, 6시 , 3시
    if n:
        new_y = y
        while new_y >= 0:
            if (new_y, x) in arr[6]:
                break
            DP[new_y][x] = True
            new_y -= 1
    if w:
        new_x = x
        while new_x >= 0:
            if (y, new_x) in arr[6]:
                break
            DP[y][new_x] = True
            new_x -= 1
    if s:
        new_y = y
        while new_y < N:
            if (new_y, x) in arr[6]:
                break
            DP[new_y][x] = True
            new_y += 1
    if e:
        new_x = x
        while new_x < M:
            if (y, new_x) in arr[6]:
                break
            DP[y][new_x] = True
            new_x += 1


products = []
s = ""
for i in arr:
    if i < 6:
        for j in arr[i]:
            s += "combin[" + str(i - 1) + "]"
            products.append(j)
            s += ","
result = sys.maxsize
for e in eval("list(itertools.product(" + s.strip(",") + "))"):
    print(e)
    total = M*N # 모든 사각지대
    DP = [[False] * M for _ in range(N)]
    for i, j in enumerate(e):
        camera(products[i], j)
    for d in DP:
        for z in d:
            if z:
                total-=1
    result = min(result, total-len(arr[6])) #벽을 빼준 나머지

print(result)
