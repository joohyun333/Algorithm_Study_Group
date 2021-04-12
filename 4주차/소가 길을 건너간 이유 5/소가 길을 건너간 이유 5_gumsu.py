n, k, b = map(int, input().split())
road = [False for _ in range(n+1)]
for _ in range(b):
    tmp = int(input())
    road[tmp] = True

res = 10e9
for i in range(1, n-k+2):
    cnt = 0
    for j in range(i, i+k):
        if road[j]:
            cnt += 1
    res = min(res, cnt)
print(res)