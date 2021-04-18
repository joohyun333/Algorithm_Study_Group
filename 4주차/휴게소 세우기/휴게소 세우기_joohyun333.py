# https://www.acmicpc.net/problem/1477
import sys
input = sys.stdin.readline
N, M, L = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [L]
arr.sort()

interval = []
for i in range(1, N + 2):
    interval.append(arr[i] - arr[i - 1])
interval.sort()
start = 1
end = interval[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in interval:
        for j in range(mid , i, mid):
            count += 1
    if count <= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
print(result)
