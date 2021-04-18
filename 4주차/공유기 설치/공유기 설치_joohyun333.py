# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
arr = [int(input()) for i in range(N)]
arr.sort()
answer = 0
start = 1
end = arr[N-1]
while start <= end:
    mid = (start + end) // 2
    first = arr[0]
    wifi = 1
    for i in range(N):
        if arr[i] >= first + mid:
            first = arr[i]
            wifi += 1
    if wifi < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)
