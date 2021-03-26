dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
arr.insert(0, ['.']*c)
arr.append(['.']*c)
for i in range(r+2):
    arr[i].insert(0, '.')
    arr[i].append('.')

# x 땅 . 바다
tmp = []
for i in range(1, r+1):
    for j in range(1, c+1):
        if arr[i][j] == 'X':
            cnt = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if arr[x][y] == '.':
                    cnt += 1
                if cnt >= 3:
                    tmp.append((i, j))


for i, j in tmp:
    arr[i][j] = '.'

rx, ry, cx, cy = 100, 100, 0, 0

for i in range(1, r+1):
    for j in range(1, c+1):
        if arr[i][j] == 'X':
            rx, ry = min(rx, i), min(ry, j)
            cx, cy = max(cx, i), max(cy, j)

# print(rx, ry, cx, cy)
for i in range(rx, cx+1):
    for j in range(ry, cy+1):
        print(arr[i][j], end='')
    print()