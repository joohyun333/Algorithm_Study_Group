# https://www.acmicpc.net/problem/13397
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    min_num, max_num = arr[0], arr[0]
    count = 1
    for i in range(N):
        min_num = min(arr[i], min_num)
        max_num = max(arr[i], max_num)
        if max_num - min_num > mid:
            count += 1
            max_num = arr[i]
            min_num = arr[i]
    if count <= M:
        end = mid - 1
        result = mid

    else:
        start = mid + 1
print(result)